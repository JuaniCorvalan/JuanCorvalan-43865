from django.db import models

# Create your models here.

class ZonaNorte(models.Model):
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    deporte = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.localidad}"
    
class ZonaOeste(models.Model):
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    deporte = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.localidad}"

class ZonaSur(models.Model):
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    deporte = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.localidad}"

class Caba(models.Model):
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    deporte = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.localidad}"