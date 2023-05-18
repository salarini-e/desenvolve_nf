from django.shortcuts import render

def index(request):
    context = {
        'titulo':'Sistema de Estágio',
    }
    return render(request, 'estagio/index.html', context)

def vagas(request):
    context = {
        'titulo':'Vagas de Estágio'
    }
    return render(request, 'estagio/vagas.html', context)

def secretaria(request):
    context = {
        'titulo':'Secretaria'
    }
    return render(request, 'estagio/secretaria.html', context)