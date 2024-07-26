from django.shortcuts import render
from django.http import HttpResponse
from AppKyle.forms import ArticulosFormAlta, ArticulosFormBusca
from AppKyle.models import Articulos

# Create your views here.
def inicio(request):
    return render(request, "AppKyle/index.html")

def articulos(request):
    return render(request, "AppKyle/articulos.html")

def gastos(request):
    return render(request, "AppKyle/gastos.html")

def clientes(request):
    return render(request, "AppKyle/clientes.html")

def agregarArticulos(request):
    if request.method == "POST":
        miFormulario = ArticulosFormAlta(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulos(producto=informacion["producto"], precio=informacion["precio"])
            articulo.save()
            return render(request, "AppKyle/articuloAgregado.html", {"articulo": articulo})
    else:
        miFormulario = ArticulosFormAlta()

    return render(request, "AppKyle/agregarArticulos.html", {"miFormulario": miFormulario})



def buscarArticulos(request):
    if request.method == "POST":
        miFormulario = ArticulosFormBusca(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulos.objects.filter(producto__icontains=informacion["producto"])
            buscaste = informacion["producto"]
            return render(request, "AppKyle/resultado_busca_articulos.html", {"articulo": articulo})
    else:
        miFormulario = ArticulosFormBusca()

    return render(request, "AppKyle/buscarArticulos.html", {"miFormulario": miFormulario})

