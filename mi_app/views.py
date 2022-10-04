from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,
                  "mi_app/index.html",
                  {"variable1": "Valor de v1",
                   "variable2": "Valor de v2"})


def otra_vista(request, parametro):
    print(type(parametro))
    return HttpResponse("Esta es una segunda vista " + str(parametro))