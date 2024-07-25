from django.urls import path
from AppKyle import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('articulos/', views.articulos, name='Articulos'),
    path('gastos/', views.gastos, name='Gastos'),
    path('clientes/', views.clientes, name='Clientes'),
    
]