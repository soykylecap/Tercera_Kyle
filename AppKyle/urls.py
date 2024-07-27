from django.urls import path
from AppKyle import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('articulos/', views.articulos, name='Articulos'),
    path('gastos/', views.gastos, name='Gastos'),
    path('clientes/', views.clientes, name='Clientes'),
    
]

urlpatterns += [
    path('articulos/articulos_agregar/', views.agregarArticulos, name='AgregarArticulos'),
    path('articulos/articulos_buscar/', views.buscarArticulos, name='BuscarArticulos'),
    path('clientes/clientes_agregar/', views.agregarClientes, name='AgregarClientes'),
    path('clientes/clientes_buscar/', views.buscarClientes, name='BuscarClientes'),
    path('gastos/gastos_agregar/', views.agregarGastos, name='AgregarGastos'),
    path('gastos/gastos_buscar/', views.buscarGastos, name='BuscarGastos'),
    
]