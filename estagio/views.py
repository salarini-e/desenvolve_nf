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

def listar_candidato(request):
    context = {
        'titulo':'Secretaria',
        'estudante': Estudante.objects.filter(status=0),
    }
    return render(request, 'estagio/listar_estudantes.html', context)

def listar_estagiario(request):
    context = {
        'titulo':'Secretaria',
        'estudante': Estudante.objects.filter(status=1), 
    }
    return render(request, 'estagio/listar_estudantes.html', context)
