from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(response):
    return HttpResponse("Hola! Bienvenidos a Django")


def otra_vista(response):
    return HttpResponse("Esta es una segunda vista")