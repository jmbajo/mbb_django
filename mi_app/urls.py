from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("otra/", views.otra_vista, name="otra_vista")
]