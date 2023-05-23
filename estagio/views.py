from django.shortcuts import render
from .models import Vagas, Estudante

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
        'aluno': Estudante.objects.all(),
 
    }
    return render(request, 'estagio/secretaria.html', context)
