from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import PredictionLog, FeedbackEntry, PublicPredictionLog, PublicFeedbackEntry


@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = ("id", "model_used", "predicted_label", "confidence", "created_at", "has_feedback")
    list_filter = ("model_used", "predicted_label")
    search_fields = ("input_text",)
    readonly_fields = ("created_at",)

    def has_feedback(self, obj):
        return hasattr(obj, "feedback")
    has_feedback.boolean = True
    has_feedback.short_description = "Feedback?"


@admin.register(FeedbackEntry)
class FeedbackEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "get_input_text", "get_predicted", "correct_label", "is_exported", "submitted_at")
    list_filter = ("correct_label", "is_exported")
    actions = ["export_as_csv"]

    def get_input_text(self, obj):
        return obj.prediction.input_text[:60]
    get_input_text.short_description = "Input Text"

    def get_predicted(self, obj):
        return obj.prediction.predicted_label
    get_predicted.short_description = "Predicted"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="selected_feedback.csv"'
        writer = csv.writer(response)
        writer.writerow(["input_text", "predicted_label", "correct_label", "model_used", "notes"])
        for entry in queryset.select_related("prediction"):
            writer.writerow([
                entry.prediction.input_text,
                entry.prediction.predicted_label,
                entry.correct_label,
                entry.prediction.model_used,
                entry.notes,
            ])
        return response
    export_as_csv.short_description = "Export selected as CSV"


@admin.register(PublicPredictionLog)
class PublicPredictionLogAdmin(admin.ModelAdmin):
    list_display = ("id", "model_used", "predicted_label", "confidence", "created_at", "has_feedback")
    list_filter = ("model_used", "predicted_label")
    search_fields = ("input_text",)
    readonly_fields = ("created_at",)

    def has_feedback(self, obj):
        return hasattr(obj, "feedback")
    has_feedback.boolean = True
    has_feedback.short_description = "Feedback?"


@admin.register(PublicFeedbackEntry)
class PublicFeedbackEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "get_input_text", "get_predicted", "correct_label", "is_exported", "submitted_at")
    list_filter = ("correct_label", "is_exported")
    
    def get_input_text(self, obj):
        return obj.prediction.input_text[:60]
    get_input_text.short_description = "Input Text"

    def get_predicted(self, obj):
        return obj.prediction.predicted_label
    get_predicted.short_description = "Predicted"

