from django import forms

class ArticulosFormAlta(forms.Form):
    producto = forms.CharField(max_length=25)
    precio = forms.FloatField()

class ArticulosFormBusca(forms.Form):
    producto = forms.CharField()

class ClientesFormAlta(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class ClientesFormBusca(forms.Form):
    nombre = forms.CharField(max_length=40, required=False)
    apellido = forms.CharField(max_length=40, required=False)



