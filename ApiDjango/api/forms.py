from django import forms
from .models import RegistroCliente
from .models import registroProblemas

class Registro_Cliente(forms.ModelForm):
    class Meta:
        model = RegistroCliente
        fields = ['Nombre','Apellidos','Usuario','password','Correo','CP','Telefono','Direccion']

class ProblemasCliente(forms.ModelForm):
    class Meta:
        model = registroProblemas
        fields = ['Nombre','Direccion','ProblemaC']