from django.shortcuts import render, redirect
from .models import *
from autenticacao.models import Pessoa
from .forms import *
def index(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
    }
    return render(request, 'estagio/index.html', context)

def vagas(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'vagas': Vagas.objects.all()
    }
    return render(request, 'estagio/vagas.html', context)

def listar_candidato(request):
    context = {
         'titulo':'Programa de Estágio para Estudantes',
        'estudante': Estudante_Vaga.objects.filter(status=0),
    }
    return render(request, 'estagio/listar_estudantes.html', context)

def listar_estagiario(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'estudante': Estudante_Vaga.objects.filter(status=1), 
        'supervisor': True
    }
    return render(request, 'estagio/listar_estudantes.html', context)

def candidatar_se_vaga(request, id):
    pessoa = Pessoa.objects.get(user=request.user)
    
    try:
        instance=Estudante.objects.get(pessoa=pessoa)
        forms_estudante = Estudante_form(instance=instance, initial={'universidade': instance.universidade.id, 'curso': instance.curso.id})
    except:
        forms_estudante = Estudante_form(initial={'pessoa': pessoa.id})

    vaga =  Vagas.objects.get(id=id)
    forms_vaga = Estudante_vaga_form(initial={'status': 0, 'vaga': id})

    if request.method == 'POST':
        if instance:
             forms_estudante = Estudante_form(request.POST, instance=instance)
        else:
            forms_estudante = Estudante_form(request.POST)

        forms_vaga = Estudante_vaga_form(request.POST)
        
        if forms_estudante.is_valid():
            estudante=forms_estudante.save()
            estudante.pessoa=pessoa
            estudante.save()
            if  forms_vaga.is_valid(estudante):
                estudante_vaga=forms_vaga.save(commit=False)
                estudante_vaga.estudante=estudante
                estudante_vaga.status='0'
                estudante_vaga.vaga=vaga
                estudante_vaga.save()
    context = {
        'forms_estudante': forms_estudante,
        'forms_vaga': forms_vaga,
        'vaga': vaga
    }
    return render(request, 'estagio/candidatar_se_vaga.html', context)

def editar_estudante(request, id):
    instance = Estudante_Vaga.objects.get(id=id)
    forms = Editar_estudante_forms(instance=instance)
    if request.method == 'POST':
        forms = Editar_estudante_forms(request.POST, instance=instance)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms
    }
    return render(request, 'estagio/editar_estudante.html', context)

def cadastro_vaga(resquest):
    forms = Cadatrar_Vaga_form()
    if resquest.method == 'POST':
        forms = Cadatrar_Vaga_form(resquest.POST, resquest.FILES)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms,
        'titulo':'Programa de Estágio para Estudantes',
    }
    return render(resquest, 'estagio/cadastrar_vagas.html', context)

def cadastrar_universidade(request):
    forms = Universidade_form()
    if request.method == 'POST':
        forms = Universidade_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms,
        'titulo':'Programa de Estágio para Estudantes',
    }
    return render(request, 'estagio/cadastrar_universidade.html', context)

def listar_universidade(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'universidades': Universidade.objects.all(),
    }
    return render(request, 'estagio/universidade.html', context)

def cadastrar_curso(request, id):
    forms = Curso_form(initial={
        'universidade':id,
    })
    if request.method == 'POST':
        # Valida o id no form se n vai dar merda
        forms = Curso_form(request.POST)
        if forms.is_valid():
            curso = forms.save()
            curso.universidade = Universidade.objects.get(id=id)
            curso.save()
            return redirect('estagio:curso', id)
    context={
        'titulo':'Programa de Estágio para Estudantes',
        'forms':forms,
        'id': id
    }
    return render(request, 'estagio/cadastrar_curso.html', context)

def listar_curso(request, id):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'cursos':Curso.objects.filter(universidade__id=id),
        'id': id
    }
    return render(request, 'estagio/cursos.html', context)

def listar_supervisor(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'supervisores':Supervisor.objects.all(),
    }
    return render(request, 'estagio/supervisor.html', context)

def cadastrar_supervisor(request):
    forms = Supervisor_form()
    if request.method == 'POST':
        forms = Supervisor_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms
    }
    return render(request, 'estagio/cadastrar_supervisor.html', context)

def listar_secretaria(request):
    context = {
        'titulo':'Programa de Estágio para Estudantes',
        'secretarias':Secretaria.objects.all(),
    }
    return render(request, 'estagio/secretaria.html', context)

def cadastrar_secretaria(request):
    forms = Secretaria_form()
    if request.method == 'POST':
        forms = Secretaria_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms
    }
    return render(request, 'estagio/cadastrar_secretaria.html', context)