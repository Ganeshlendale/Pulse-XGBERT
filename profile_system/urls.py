from django.urls import path
from . import views

app_name = 'profile_system'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_detail_view, name='profile_detail'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('profile/change-password/', views.change_password_view, name='change_password'),
    path('profile/delete-account/', views.delete_account_view, name='delete_account'),
]
