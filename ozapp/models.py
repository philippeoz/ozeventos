from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    idade_minima = models.IntegerField()
    idade_maxima = models.IntegerField()
    data_criacao = models.DateTimeField(default=timezone.now, null=True)
    data_inicio = models.DateTimeField(blank=True)
    data_fim = models.DateTimeField(blank=True)
    local = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.IntegerField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    # criador = models.ForeignKey('auth.User', blank=True)
    teste = []
    administradores = models.ManyToManyField(User, related_name='administradores')
    participantes = models.ManyToManyField(User, related_name='participantes')


    def __str__(self):
        return self.nome
