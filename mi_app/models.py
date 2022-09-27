from django.db import models

# Create your models here.
# LsitaDeTareas esta descripta por su nombre
class ListaDeTareas(models.Model):
    nombre = models.CharField(max_length=100)


class Tarea(models.Model):
    lista_de_tareas = models.ForeignKey(ListaDeTareas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    completa = models.BooleanField()

