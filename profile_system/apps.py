# from django.apps import AppConfig


# class ProfileSystemConfig(AppConfig):
#     name = 'profile_system'

#########################
from django.apps import AppConfig


class ProfileSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_system'
    verbose_name = 'Profile System'

    def ready(self):
        import profile_system.models  # noqa: F401 — ensures signals are registered
