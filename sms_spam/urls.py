"""
URL configuration for sms_spam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#for the profile system
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    #pages
    path('pages/', include('pages.urls')),
    #account
    path('account/', include('profile_system.urls')),
    #model
    path("model/", include("model_app.urls", namespace="model_app")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
