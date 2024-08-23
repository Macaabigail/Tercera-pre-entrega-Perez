from django.db import models

# Create your models here.
class Base(models.Model):
    nombre = models.CharField(max_length=40)
    

class Guarda(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    
class Conductor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)

class Operador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)