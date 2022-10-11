from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def alta(request):
    if request.method == "POST": # proceso el form de creación de usuario
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tareas/')
    else:
        form = UserCreationForm()
        return render(request, "registration/alta.html", {'form': form})