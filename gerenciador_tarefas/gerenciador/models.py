from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tarefa(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
