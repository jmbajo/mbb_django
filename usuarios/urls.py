from django.contrib import admin
from django.urls import path, include

from usuarios import views

urlpatterns = [
    path("create/", views.alta, name="alta_usuario"),
]
