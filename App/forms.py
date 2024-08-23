from django import forms 

class Baseformulario (forms.Form):
       base = forms.CharField(max_length=20)
       
       
       
class Guardaformulario (forms.Form):
       nombre = forms.CharField(max_length=20)
       apellido = forms.CharField(max_length=20)
       categoria = forms.CharField(max_length=20)
       
       
class Conductoresformulario (forms.Form):
       nombre = forms.CharField(max_length=20)
       apellido = forms.CharField(max_length=20)
       categoria = forms.CharField(max_length=20)
       
       
class Operadoresformulario(forms.Form):
       nombre = forms.CharField(max_length=20)
       apellido = forms.CharField(max_length=20)
       categoria = forms.CharField(max_length=20)
       
       
class Buscar(forms.Form):
       nombre = forms.CharField(max_length=20)
