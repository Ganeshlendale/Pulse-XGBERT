from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('shield/', views.sms_shield, name='sms_shield'),
    path('shield/insights/', views.model_insights, name='model_insights'),
    path('shield/database/', views.database_records, name='database_records'),
]
