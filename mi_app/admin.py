from django.contrib import admin

# Register your models here.
from mi_app.models import ListaDeTareas, Tarea

admin.site.register(ListaDeTareas)
admin.site.register(Tarea)

