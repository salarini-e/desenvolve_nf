from django.shortcuts import render
from .models import Vagas, Curso, Secretaria, Universidade

def index(request):
    universidadeCad = Universidade(nome='CEFET')
    universidadeCad.save()

    secretariaCad = Secretaria(nome='Secretaria de Ciências', local='Prefeitura')
    secretariaCad.save()

    cursoCad = Curso(nome='Sistemas da Informação', curso_id_universidade=universidadeCad)
    cursoCad.save()

    vagasCad = Vagas(nome='Desenvolvimento Web', quantidade_de_vagas=5, vagas_id_secretaria=secretariaCad)
    vagasCad.save()
    vagasCad.vagas_id_curso.add(cursoCad)
    vagasCad.save()

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
