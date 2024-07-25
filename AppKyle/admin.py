from django.contrib import admin
from .models import Articulos, Gastos, Clientes

# Register your models here.

admin.site.register(Articulos)
admin.site.register(Gastos)
admin.site.register(Clientes)

