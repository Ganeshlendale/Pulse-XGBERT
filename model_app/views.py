from django.shortcuts import render

# Create your views here.
import csv
import logging

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import FeedbackForm, PredictForm
from .ml_engine import distilbert_predict, xgb_predict
from .models import FeedbackEntry, PredictionLog, PublicPredictionLog, PublicFeedbackEntry

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Home / predict
# ---------------------------------------------------------------------------

def index(request):
    """Landing page with the prediction form."""
    form = PredictForm()
    if request.user.is_authenticated:
        recent = PredictionLog.objects.filter(user=request.user).select_related("feedback").order_by("-created_at")[:10]
    else:
        recent = PublicPredictionLog.objects.all().select_related("feedback").order_by("-created_at")[:10]
    return render(request, "model_app/index.html", {"form": form, "recent": recent})


def predict(request):
    """Handle prediction POST; returns JSON for AJAX or redirects for plain form."""
    if request.method != "POST":
        return redirect("model_app:index")

    form = PredictForm(request.POST)
    if not form.is_valid():
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"error": form.errors}, status=400)
        messages.error(request, "Invalid form input.")
        return redirect("model_app:index")

    text = form.cleaned_data["text"].strip()
    model_choice = form.cleaned_data["model_choice"]

    try:
        if model_choice == "distilbert":
            result = distilbert_predict(text)
        else:
            result = xgb_predict(text)
    except Exception as exc:
        logger.exception("Prediction error")
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"error": str(exc)}, status=500)
        messages.error(request, f"Prediction failed: {exc}")
        return redirect("model_app:index")

    if request.user.is_authenticated:
        log = PredictionLog.objects.create(
            input_text=text,
            predicted_label=result["label"],
            confidence=result.get("confidence"),
            model_used=model_choice,
            user=request.user,
        )
    else:
        log = PublicPredictionLog.objects.create(
            input_text=text,
            predicted_label=result["label"],
            confidence=result.get("confidence"),
            model_used=model_choice,
        )

    payload = {
        "prediction_id": log.pk,
        "label": result["label"],
        "confidence": result.get("confidence"),
        "all_probs": result.get("all_probs", {}),
        "model_used": model_choice,
    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse(payload)

    return render(
        request,
        "model_app/result.html",
        {"result": payload, "input_text": text, "feedback_form": FeedbackForm()},
    )


# ---------------------------------------------------------------------------
# Feedback
# ---------------------------------------------------------------------------

def submit_feedback(request, prediction_id):
    if request.user.is_authenticated:
        log = get_object_or_404(PredictionLog, pk=prediction_id, user=request.user)
        FeedbackModel = FeedbackEntry
    else:
        log = get_object_or_404(PublicPredictionLog, pk=prediction_id)
        FeedbackModel = PublicFeedbackEntry

    if hasattr(log, "feedback"):
        messages.info(request, "Feedback already recorded for this prediction.")
        return redirect("model_app:index")

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            FeedbackModel.objects.create(
                prediction=log,
                correct_label=form.cleaned_data["correct_label"],
                notes=form.cleaned_data.get("notes", ""),
            )
            messages.success(request, "Thank you! Your feedback has been saved.")
            return redirect("model_app:index")
    else:
        form = FeedbackForm()

    return render(
        request,
        "model_app/feedback.html",
        {"form": form, "log": log},
    )


# ---------------------------------------------------------------------------
# History & export
# ---------------------------------------------------------------------------

def history(request):
    if request.user.is_authenticated:
        logs = PredictionLog.objects.filter(user=request.user).select_related("feedback").order_by("-created_at")
    else:
        logs = PublicPredictionLog.objects.all().select_related("feedback").order_by("-created_at")
    return render(request, "model_app/history.html", {"logs": logs})


def export_feedback_csv(request):
    """Download all feedback entries as a CSV for retraining."""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="feedback_training_data.csv"'

    writer = csv.writer(response)
    writer.writerow(["id", "input_text", "predicted_label", "correct_label", "model_used", "submitted_at", "notes"])

    if request.user.is_authenticated:
        entries = FeedbackEntry.objects.filter(prediction__user=request.user).select_related("prediction").order_by("submitted_at")
    else:
        entries = PublicFeedbackEntry.objects.all().select_related("prediction").order_by("submitted_at")
    for entry in entries:
        writer.writerow([
            entry.pk,
            entry.prediction.input_text,
            entry.prediction.predicted_label,
            entry.correct_label,
            entry.prediction.model_used,
            entry.submitted_at.isoformat(),
            entry.notes,
        ])
        entry.is_exported = True
        entry.save(update_fields=["is_exported"])

    return response


# ---------------------------------------------------------------------------
# REST API endpoint (lightweight, no DRF needed)
# ---------------------------------------------------------------------------

def api_predict(request):
    """
    POST /api/predict/
    Body (JSON): {"text": "...", "model": "xgboost" | "distilbert"}
    Returns JSON with label, confidence, all_probs, prediction_id.
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    import json
    try:
        body = json.loads(request.body)
    except Exception:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    text = body.get("text", "").strip()
    model_choice = body.get("model", "xgboost")

    if not text:
        return JsonResponse({"error": "text field is required"}, status=400)

    try:
        result = distilbert_predict(text) if model_choice == "distilbert" else xgb_predict(text)
    except Exception as exc:
        logger.exception("API prediction error")
        return JsonResponse({"error": str(exc)}, status=500)

    if request.user.is_authenticated:
        log = PredictionLog.objects.create(
            input_text=text,
            predicted_label=result["label"],
            confidence=result.get("confidence"),
            model_used=model_choice,
            user=request.user,
        )
    else:
        log = PublicPredictionLog.objects.create(
            input_text=text,
            predicted_label=result["label"],
            confidence=result.get("confidence"),
            model_used=model_choice,
        )

    return JsonResponse({
        "prediction_id": log.pk,
        "label": result["label"],
        "confidence": result.get("confidence"),
        "all_probs": result.get("all_probs", {}),
        "model_used": model_choice,
    })
