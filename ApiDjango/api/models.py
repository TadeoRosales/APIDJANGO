from django.db import models

# Create your models here.

class RegistroCliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    CP = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)

class registroProblemas(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    ProblemaC = models.CharField(max_length=100)