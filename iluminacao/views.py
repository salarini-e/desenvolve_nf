from django.shortcuts import render, redirect
from .forms import *
from autenticacao.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    return render(request, 'os_index.html')

def os_index(request):
    data=OrdemDeServico.objects.all()
    paginator = Paginator(data, 30)
    page = request.GET.get('page', 1)
    ordens_de_servico = paginator.get_page(page)
    
    context={
        'ordens_de_servico': ordens_de_servico
    }
    return render(request, 'iluminacao/index.html', context)


@login_required
def add_os(request):
    
    form = OS_Form()

    if request.method=='POST':
        form=OS_Form(request.POST)
        if form.is_valid():
            os=form.save(commit=False)
            os.contribuinte=Pessoa. objects.get(user=request.user)
            os.save()

            return redirect('index')
            
        print(form.erros)


    context={
        'form': form
    }

    return render(request, 'iluminacao/adicionar_os.html', context)


def detalhes_os(request, id):
    os=OrdemDeServico.objects.get(id=id)
    if request.method=='POST':        
        pass
    else:
        pass
    context={
        'os': os
    }
    return render(request, 'iluminacao/detalhes_os.html', context)

def funcionarios_listar(request):
    funcionarios=Funcionario_OS.objects.all()
    context={
        'funcionarios': funcionarios
    }
    return render(request, 'equipe/funcionarios.html', context)

def funcionario_cadastrar(request):
    if request.method=='POST':
        form=Funcionario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    else:
        form=Funcionario_Form()
        context={
            'form': form
        }
    return render(request, 'equipe/funcionarios_cadastrar.html', context)

def funcionario_editar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    form=Funcionario_Form(instance=funcionario)
    if request.method=='POST':
        form=Funcionario_Form(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    context={
        'form': form,
        'funcionario': funcionario
    }     
    return render(request, 'equipe/funcionarios_editar.html', context)

def funcionario_deletar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    funcionario.delete()

    return redirect('funcionarios')

def atribuir_equipe(request, id):
    try:
        instancia=OS_ext.objects.get(os=id)
        form=Equipe_Form(instance=instancia)        
    except Exception as e:
        form=Equipe_Form(initial={'os': id})
        instancia=None
        
    if request.method=='POST':
        if instancia:
            form=Equipe_Form(request.POST, instance=instancia)
        else:
            form=Equipe_Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('detalhes_os', id)
    context={
            'form':form,
        }
    return render(request, 'iluminacao/adicionar_ext.html', context)