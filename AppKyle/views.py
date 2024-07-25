from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppKyle/index.html")

def articulos(request):
    return render(request, "AppKyle/articulos.html")

def gastos(request):
    return render(request, "AppKyle/gastos.html")

def clientes(request):
    return render(request, "AppKyle/clientes.html")