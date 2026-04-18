from django.urls import path
from . import views

app_name = "model_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict, name="predict"),
    path("feedback/<int:prediction_id>/", views.submit_feedback, name="feedback"),
    path("history/", views.history, name="history"),
    path("export/feedback/", views.export_feedback_csv, name="export_feedback"),
    # REST API
    path("api/predict/", views.api_predict, name="api_predict"),
]
