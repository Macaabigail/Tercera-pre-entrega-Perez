from django.db import models

# Create your models here.
class Base(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre:{self.nombre}"
           
    

class Guarda(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre:{self.nombre} - apellido:{self.apellido} - categoria:{self.categoria}"
    
class Conductor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre:{self.nombre} - apellido:{self.apellido} - categoria:{self.categoria}"

class Operador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre:{self.nombre} - apellido:{self.apellido} - categoria:{self.categoria}"