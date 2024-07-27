from django.shortcuts import render
from django.http import HttpResponse
from AppKyle.forms import ArticulosFormAlta, ArticulosFormBusca, ClientesFormAlta, ClientesFormBusca, GastosFormAlta, GastosFormBusca
from AppKyle.models import Articulos, Clientes, Gastos
from datetime import datetime

# Create your views here.
def inicio(request):
    return render(request, "AppKyle/index.html")

def articulos(request):
    return render(request, "AppKyle/articulos.html")

def gastos(request):
    return render(request, "AppKyle/gastos.html")

def clientes(request):
    return render(request, "AppKyle/clientes.html")


#Articulos
#-----------------------------------------------------------------------------------

def agregarArticulos(request):
    if request.method == "POST":
        miFormulario = ArticulosFormAlta(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulos(producto=informacion["producto"], precio=informacion["precio"])
            articulo.save()
            return render(request, "AppKyle/articulos_agregar_ok.html", {"articulo": articulo})
    else:
        miFormulario = ArticulosFormAlta()

    return render(request, "AppKyle/articulos_agregar.html", {"miFormulario": miFormulario})


def buscarArticulos(request):
    if request.method == "POST":
        miFormulario = ArticulosFormBusca(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulos.objects.filter(producto__icontains=informacion["producto"])
            buscaste = informacion["producto"]
            return render(request, "AppKyle/articulos_buscar_resultados.html", {"articulo": articulo})
    else:
        miFormulario = ArticulosFormBusca()

    return render(request, "AppKyle/articulos_buscar.html", {"miFormulario": miFormulario})


#Clientes
#-----------------------------------------------------------------------------------

def agregarClientes(request):
    if request.method == "POST":
        miFormulario = ClientesFormAlta(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = Clientes(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            cliente.save()
            return render(request, "AppKyle/clientes_agregar_ok.html", {"cliente": cliente})
    else:
        miFormulario = ClientesFormAlta()

    return render(request, "AppKyle/clientes_agregar.html", {"miFormulario": miFormulario})


def buscarClientes(request):
    if request.method == "POST":
        miFormulario = ClientesFormBusca(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(informacion["nombre"])

            if informacion["nombre"] != "":
                cliente = Clientes.objects.filter(nombre__icontains=informacion["nombre"])
                print(cliente)
                return render(request, "AppKyle/clientes_buscar_resultados.html", {"cliente":cliente})
            elif informacion["apellido"] != "":
                cliente = Clientes.objects.filter(apellido__icontains=informacion["apellido"])
                print(cliente)
                return render(request, "AppKyle/clientes_buscar_resultados.html", {"cliente":cliente})
            else:
                miFormulario = ClientesFormBusca()
    else:
        miFormulario = ClientesFormBusca()

    return render(request, "AppKyle/clientes_buscar.html", {"miFormulario": miFormulario})


#Gastos
#-----------------------------------------------------------------------------------

def agregarGastos(request):
    if request.method == "POST":
        miFormulario = GastosFormAlta(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            gasto = Gastos(fecha=informacion["fecha"], detalle=informacion["detalle"], area=informacion["area"], importe=informacion["importe"])
            gasto.save()
            return render(request, "AppKyle/gastos_agregar_ok.html", {"gasto": gasto})
    else:
        miFormulario = GastosFormAlta(initial={'fecha': datetime.now().date()})

    return render(request, "AppKyle/gastos_agregar.html", {"miFormulario": miFormulario})


def buscarGastos(request):
    if request.method == "POST":
        miFormulario = GastosFormBusca(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            gastos = Gastos.objects.filter(area=informacion["area"])
            return render(request, "AppKyle/gastos_buscar_resultados.html", {"gastos":gastos})
    else:
        miFormulario = GastosFormBusca()
    return render(request, "AppKyle/gastos_buscar.html", {"miFormulario": miFormulario})

