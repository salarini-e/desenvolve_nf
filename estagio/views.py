from django.shortcuts import render
from .models import Vagas, Estudante_Vaga, Estudante
from autenticacao.models import Pessoa
from .forms import Estudante_form, Estudante_vaga_form, Editar_estudante_forms

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
        'estudante': Estudante_Vaga.objects.filter(status=0),
    }
    return render(request, 'estagio/listar_estudantes.html', context)

def listar_estagiario(request):
    context = {
        'titulo':'Secretaria',
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