from django import forms

class ArticulosFormAlta(forms.Form):
    producto = forms.CharField(max_length=25)
    precio = forms.FloatField()


class ArticulosFormBusca(forms.Form):
    producto = forms.CharField()

class GastosFormAlta(forms.Form):
    fecha = forms.DateField()
    detalle = forms.CharField(max_length=30)
    area = forms.CharField()
    importe = forms.FloatField()

class ClientesFormAlta(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()


