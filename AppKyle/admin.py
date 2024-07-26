from django.contrib import admin
from .models import Articulos, Gastos, Clientes

# Register your models here.

admin.site.register(Articulos)
admin.site.register(Gastos)
admin.site.register(Clientes)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'producto', 'precio')
    ordering = ('id')
