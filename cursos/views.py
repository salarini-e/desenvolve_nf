from multiprocessing import context
from django.shortcuts import render
from .models import Categoria, Curso
def index(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    categorias=Categoria.objects.all()
    cursos=[]
    for i in categorias:
        cursos.append({'categoria':i, 'curso':Curso.objects.filter(categoria=i, ativo=True)})

    context={
        'categorias': cursos
    }
    return render(request, 'cursos/cursos.html', context)

def prematricula(request):
    return render(request, 'cursos/pre_matricula.html')

def alterarCad(request):
    return render(request, 'cursos/alterar_cad.html')

def resultado(request):
    return render(request, 'cursos/resultado.html')