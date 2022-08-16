from django.shortcuts import render

def index(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    return render(request, 'cursos/cursos.html')

def prematricula(request):
    return render(request, 'cursos/pre_matricula.html')

def alterarCad(request):
    return render(request, 'cursos/alterar_cad.html')

def resultado(request):
    return render(request, 'cursos/resultado.html')