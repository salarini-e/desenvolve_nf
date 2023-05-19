from django.shortcuts import render
from .models import Vagas, Curso, Secretaria, Universidade

def index(request):
    context = {
        'titulo':'Sistema de Estágio',
    }
    return render(request, 'estagio/index.html', context)

def vagas(request):
    context = {
        'titulo':'Vagas de Estágio',
        'vagas': Vagas.objects.all()
    }
    return render(request, 'estagio/vagas.html', context)

def secretaria(request):
    context = {
        'titulo':'Secretaria',
        'secretarias': Secretaria.objects.all()
    }
    return render(request, 'estagio/secretaria.html', context)
