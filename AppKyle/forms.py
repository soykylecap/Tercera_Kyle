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

class GastosFormAlta(forms.Form):
    fecha = forms.DateField()
    detalle = forms.CharField(max_length=30)
    area = forms.CharField(max_length=30, widget=forms.Select(choices=[
            ('GEN', 'Generales'),
            ('DIS', 'Distribución'),
            ('DEP', 'Depósito'),
            ('ADM', 'Administración')
        ]))
    importe = forms.FloatField()

class GastosFormBusca(forms.Form):
    area = forms.CharField(max_length=30, widget=forms.Select(choices=[
            ('GEN', 'Generales'),
            ('DIS', 'Distribución'),
            ('DEP', 'Depósito'),
            ('ADM', 'Administración')
        ]))
