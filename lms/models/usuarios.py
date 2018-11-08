from django.db import models
from datetime import date

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1), blank=True, null=True)

class Coordenador(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)

class Aluno(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)
    ra = models.CharField(max_length=20, unique=True)
    foto = models.CharField(max_length=255, default=None, blank=True, null=True)

class Professor(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)
    apelido = models.CharField(max_length=255)
