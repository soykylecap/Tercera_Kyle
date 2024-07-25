from django.db import models

# Create your models here.

class Articulos(models.Model):
    producto = models.CharField(max_length=25, help_text = "Maximo 25 caracteres")
    precio = models.FloatField()

class Gastos(models.Model):
    fecha = models.DateField(auto_now=True)
    detalle = models.CharField(max_length=30)
    area = models.CharField(max_length=30, choices=[('GEN','Generales'), ('DIS','Distribucion'), ('DEP','Deposito'), ('ADM','Administracion')])
    importe = models.FloatField()

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
