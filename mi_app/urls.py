from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("crear/", views.crear_tarea, name="crear_tarea"),
    path("lista/<int:id>", views.mostrar_lista, name="mostrar_lista"),
    path("listas/", views.mostrar_listas, name="mostrar_listas"),
]