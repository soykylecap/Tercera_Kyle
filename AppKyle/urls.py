from django.urls import path
from AppKyle import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('articulos/', views.articulos, name='Articulos'),
    path('gastos/', views.gastos, name='Gastos'),
    path('clientes/', views.clientes, name='Clientes'),
    
]

urlpatterns += [
    path('articulos/agregarArticulos/', views.agregarArticulos, name='AgregarArticulos'),
    path('articulos/buscarArticulos/', views.buscarArticulos, name='BuscarArticulos'),
    
]