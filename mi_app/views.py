from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from mi_app.forms import CrearListaForm
from mi_app.models import ListaDeTareas


def home(request):
    # Queremos mostrar las listas de un determinado usuario (el que está logueado actualmente)
    listas = request.user.listadetareas_set.all()
    return render(request, 'mi_app/mostrar_listas.html', {"listas_tareas": listas})

    # return render(request, 'mi_app/home.html', {})


def mostrar_lista(request, id):
    lista = ListaDeTareas.objects.get(id=id)
    tareas = lista.tarea_set.all()

    return render(request, 'mi_app/index.html', {"tareas":tareas})


def mostrar_listas(request):
    listas = ListaDeTareas.objects.all()

    return render(request, 'mi_app/mostrar_listas.html', {"listas_tareas": listas})



def index(request):
    return render(request,
                  "mi_app/index.html",
                  {"variable1": "Valor de v1",
                   "variable2": "Valor de v2"})


def crear_tarea(request):
    if request.method == "POST":
        print(request.POST)
        form = CrearListaForm(request.POST)

        if form.is_valid():
            # Variante 1
            # request.user.listadetareas_set.create(nombre=form.cleaned_data["nombre"])

            # Variante 2
            # lista = ListaDeTareas(nombre=form.cleaned_data["nombre"], user_id=request.user.id)
            # lista.save()

            # Variante 3
            # lista = ListaDeTareas(nombre=form.cleaned_data["nombre"])
            # lista.save()
            # request.user.listadetareas_set.add(lista)




            return redirect("/tareas")
    else:
        form = CrearListaForm()
        return render(request, "mi_app/create.html", {"form" : form})
