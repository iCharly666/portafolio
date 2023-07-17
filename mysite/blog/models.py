from pyexpat.errors import messages
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login



# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# Modelo para tareas.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name
    
# Modelo para foros

class CategoriaForo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Campo de fecha de creación
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Campo de fecha de modificación

    def __str__(self):
        return self.nombre
    

