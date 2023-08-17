from django.db import models
from django.contrib.auth.models import User

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
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self) -> str:
        return f"{self.imagen}"
    
#-------------------------------------

class Comentario(models.Model):
    zona_norte = models.ForeignKey(ZonaNorte, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  
    def __str__(self):
        return f"Comentario de {self.autor} en {self.fecha}"


