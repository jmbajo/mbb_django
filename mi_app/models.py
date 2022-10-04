from django.db import models

# Create your models here.
# LsitaDeTareas esta descripta por su nombre
class ListaDeTareas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "Lista de Tareas: {}".format(self.nombre)

    def __repr__(self):
        return self.__str__()


class Tarea(models.Model):
    lista_de_tareas = models.ForeignKey(ListaDeTareas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    completa = models.BooleanField()

    def __str__(self):
        return "Tarea: {}".format(self.titulo)

    def __repr__(self):
        return self.__str__()


