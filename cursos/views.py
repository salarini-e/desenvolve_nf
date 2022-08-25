from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import json

from .models import Candidato, Categoria, Curso, Turma
from .forms import CadastroCandidatoForm, CadastroCursoForm, CadastroCategoriaForm, CadastroLocalForm, CadastroTurmaForm


def index(request):
    return render(request, 'cursos/index.html')


def cursos(request):
    form=CadastroCandidatoForm()
    categorias=Categoria.objects.all()
    cursos=[]
    for i in categorias:
        cursos.append({'categoria':i, 'curso': Curso.objects.filter(categoria=i, ativo=True)})

    context={
        'categorias': cursos,
        'form': form
    }
    return render(request, 'cursos/cursos.html', context)

# def candidatar(request):
#     if request.method=='POST':
#         print(request.POST)
#     to_json = {
#         "key1": "value1",
#         "key2": "value2"
#     }
#     return HttpResponse(json.dumps(to_json), mimetype='application/json')                        

@login_required
def candidatar(request, id):
    
    curso=Curso.objects.get(id=id)
    form=CadastroCandidatoForm(initial={'curso': curso})
    if request.method=='POST':
        form=CadastroCandidatoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context={
        'form': form
    }               
    return render(request, 'cursos/cadastrar_candidato.html', context)    

@login_required
def cadastrar_curso(request):    
    form=CadastroCursoForm(initial={'instituicao': 1, 'user_inclusao': request.user})
    if request.method=='POST':
        form=CadastroCursoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context={
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)

@login_required
def editar_curso(request, id):    
    curso=Curso.objects.get(id=id)
    form=CadastroCursoForm(instance=curso)
    if request.method=='POST':
        form=CadastroCursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context={
        'form': form,
        'CADASTRAR': 'EDITAR'
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)

@login_required
def listar_candidatos_curso(request, id):    
    curso=Curso.objects.get(id=id)
    candidatos=Candidato.objects.filter(curso=curso)
    context={
        'candidatos': candidatos,
        'CADASTRAR': 'EDITAR',
        'curso': curso
    }
    return render(request, 'cursos/listar_candidatos_curso.html', context)

@login_required
def cadastrar_categoria(request):    
    form=CadastroCategoriaForm()
    if request.method=='POST':
        form=CadastroCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    context={
        'form': form
    }
    return render(request, 'cursos/cadastrar_categoria.html', context)

@login_required
def cadastrar_local(request):    
    form=CadastroLocalForm()
    if request.method=='POST':
        form=CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
    context={
        'form': form
    }
    return render(request, 'cursos/cadastrar_local.html', context)

def prematricula(request):
    return render(request, 'cursos/pre_matricula.html')

def alterarCad(request):
    return render(request, 'cursos/alterar_cad.html')

@login_required
def administrativo(request):
    return render(request, 'cursos/administrativo.html')

@login_required
def turmas(request):
    return render(request, 'cursos/adm_turmas.html')

def criar_turmas(request):
    form=CadastroTurmaForm(initial={'instituicao': 1, 'user_inclusao': request.user})
    if request.method=='POST':
        form=CadastroTurmaForm(request.POST)
        if form.is_valid():
            form.save()
    
        

    context={
        'form': form
    }
    return render(request, 'cursos/adm_turmas_criar.html', context)

@login_required
def listar_turmas(request):
    turmas=Turma.objects.all()
    context={
        'turmas': turmas
    }
    return render(request, 'cursos/adm_turmas_listar.html', context)

@login_required
def get_candidatos(request, id_curso):
    if request.user.is_staff:
        candidatos=Candidato.objects.filter(curso=id_curso)    
    else:
        candidatos={}
    context={
        'candidatos': candidatos
    }
    return render(request, 'cursos/GET/get_candidatos.html', context)

@login_required
def adm_cursos(request):
    return render(request, 'cursos/adm_cursos.html')

@login_required
def listar_cursos(request):
    cursos=Curso.objects.all()
    context={
        'cursos': cursos
    }
    return render(request, 'cursos/adm_cursos_listar.html', context)

def resultado(request):
    return render(request, 'cursos/resultado.html')