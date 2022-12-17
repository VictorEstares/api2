from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.


class User(AbstractUser):
    is_Alumno=models.BooleanField(default=False)
    is_Profesor=models.BooleanField(default=False)
    cI=models.CharField(max_length=20)
    def __str__(self):
        return self.username
@receiver (post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Materia (models.Model):
    nombre = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=datetime.datetime.now)
    estado = models.BooleanField(default = True)
    def __str__ (self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=datetime.datetime.now)
    estado = models.BooleanField(default = True)

    def __str__ (self):
        return self.nombre

class Alumno(models.Model):
    user=models.OneToOneField(User, related_name="Alumno", on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE,null=True)    
    def __str__(self):
        return self.user.username

class Profesor(models.Model):
    user=models.OneToOneField(User, related_name="Profesor", on_delete=models.CASCADE)
    sueldo=models.FloatField(null=True)

    def __str__(self):
        return self.user.username
    
class Administrativo(models.Model):
    user=models.OneToOneField(User, related_name="administrativo", on_delete=models.CASCADE)
    sueldo=models.FloatField(null=True)

    def __str__(self):
        return self.user.username   
    
    
class gestion (models.Model):
    nombre=models.CharField(max_length=200)
    profesor=models.ForeignKey(Profesor, on_delete=models.CASCADE,null=False)
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE,null=False)

class tipo_dato (models.Model):
    nombre=models.CharField(max_length=100)

class dato (models.Model):
    Descripcion=models.CharField(max_length=200,null=True)
    valor=models.CharField(max_length=20)
    fecha=models.DateTimeField(default=datetime.datetime.now)
    Alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,null=False)
    Gestion=models.ForeignKey(gestion, on_delete=models.CASCADE,null=False)
    Tipo=models.ForeignKey(tipo_dato,on_delete=models.CASCADE)