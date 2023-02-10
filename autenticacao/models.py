from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pessoa(models.Model):

    def __str__(self):
        return '%s' % (self.email)
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nome=models.CharField(max_length=64, verbose_name='Nome')
    email=models.EmailField()
    cpf=models.CharField(max_length=14, verbose_name='CPF', unique=True)
    telefone=models.CharField(max_length=15, verbose_name='Telefone')
    dt_nascimento=models.DateField(verbose_name='Data de nascimento')
    bairro=models.CharField(max_length=64, verbose_name='Bairro')
    endereco=models.CharField(max_length=128, verbose_name='Endereco')
    complemento=models.CharField(max_length=128, verbose_name='Complemento', blank=True, null=True)
    cep = models.CharField(max_length=9, verbose_name='CEP')
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')
