"""
URL configuration for app project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# views
from people.views import people

urlpatterns = [
    path("admin/", admin.site.urls),
    path("people/", people),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
