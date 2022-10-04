from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("otra/<parametro>", views.otra_vista, name="otra_vista"),

    path("por-defecto/", views.otra_vista, name="otra_vista2")
]