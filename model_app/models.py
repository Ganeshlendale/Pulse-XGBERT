from django.db import models
from django.contrib.auth.models import User


class PredictionLog(models.Model):
    MODEL_CHOICES = [
        ("xgboost", "XGBoost"),
        ("distilbert", "DistilBERT"),
    ]

    input_text = models.TextField(help_text="Raw text sent for prediction")
    predicted_label = models.CharField(max_length=100)
    confidence = models.FloatField(null=True, blank=True)
    model_used = models.CharField(max_length=20, choices=MODEL_CHOICES, default="xgboost")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Prediction Log"
        verbose_name_plural = "Prediction Logs"

    def __str__(self):
        return f"[{self.model_used}] {self.predicted_label} — {self.created_at:%Y-%m-%d %H:%M}"


class FeedbackEntry(models.Model):
    prediction = models.OneToOneField(
        PredictionLog,
        on_delete=models.CASCADE,
        related_name="feedback",
    )
    correct_label = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_exported = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Feedback Entry"
        verbose_name_plural = "Feedback Entries"

    def __str__(self):
        return f"Feedback #{self.pk} → {self.correct_label}"

class PublicPredictionLog(models.Model):
    MODEL_CHOICES = [
        ("xgboost", "XGBoost"),
        ("distilbert", "DistilBERT"),
    ]

    input_text = models.TextField(help_text="Raw text sent for prediction")
    predicted_label = models.CharField(max_length=100)
    confidence = models.FloatField(null=True, blank=True)
    model_used = models.CharField(max_length=20, choices=MODEL_CHOICES, default="xgboost")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Public Prediction Log"
        verbose_name_plural = "Public Prediction Logs"

    def __str__(self):
        return f"[Public-{self.model_used}] {self.predicted_label} — {self.created_at:%Y-%m-%d %H:%M}"


class PublicFeedbackEntry(models.Model):
    prediction = models.OneToOneField(
        PublicPredictionLog,
        on_delete=models.CASCADE,
        related_name="feedback",
    )
    correct_label = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_exported = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Public Feedback Entry"
        verbose_name_plural = "Public Feedback Entries"

    def __str__(self):
        return f"Public Feedback #{self.pk} → {self.correct_label}"
