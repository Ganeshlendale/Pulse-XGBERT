# from django.contrib import admin

# # Register your models here.
# ############
# from django.apps import AppConfig


# class ProfileSystemConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'profile_system'
#     verbose_name = 'Profile System'

#     def ready(self):
#         import profile_system.models  # noqa: F401 — ensures signals are registered


#####################
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'city', 'country', 'is_verified', 'created_at']
    list_filter = ['is_verified', 'gender', 'country', 'created_at']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name', 'phone_number']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Personal Info', {'fields': ('avatar', 'bio', 'gender', 'date_of_birth', 'phone_number', 'website')}),
        ('Address', {'fields': ('address', 'city', 'state', 'country', 'pincode')}),
        ('Status', {'fields': ('is_verified', 'created_at', 'updated_at')}),
    )
