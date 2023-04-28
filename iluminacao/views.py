from django.shortcuts import render, redirect
from .forms import *
from autenticacao.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.apps import apps
from .models import * 
from settings.decorators import group_required
from django.contrib.auth.models import Group
from datetime import datetime

STATUS_CHOICES=(
        ('0','Novo'),
        ('1','Aguardando'),
        ('2','Em execução'),
        ('f','Finalizado')
    )
PRIORIDADE_CHOICES=(
        ('0','Normal'),
        ('1','Moderada'),
        ('2','Urgente'),
    )

@group_required('os_acesso')
def index(request):
    return render(request, 'os_index.html')

@login_required
@group_required('os_acesso')
def os_index(request):
    if request.user.is_superuser:
        data=OrdemDeServico.objects.all()
    else:
        data=OrdemDeServico.objects.filter(contribuinte=Pessoa.objects.get(user=request.user))
    if request.method=='POST':
        valor_da_busca=request.POST['valor_da_busca']
        tipo=request.POST['tipo_da_busca']
        print(valor_da_busca, tipo)
        if tipo == 'atendente':
            data=data.filter(atendente__first_name__icontains=valor_da_busca)
        elif tipo == 'bairro':
            data=data.filter(bairro__icontains=valor_da_busca)
        elif tipo == 'data':
            try:
                valor_da_busca_date = datetime.strptime(valor_da_busca, '%d/%m/%Y').date()            
                data=data.filter(dt_solicitacao__date=valor_da_busca_date.strftime('%Y-%m-%d'))
            except:
                valores=valor_da_busca.split('/')
                print(valores)
                data=data.filter(dt_solicitacao__year=valores[1], dt_solicitacao__month=valores[0])
        elif tipo == 'protocolo':
            data=data.filter(numero__icontains=valor_da_busca)
        elif tipo == 'rua':
            data=data.filter(logradouro__icontains=valor_da_busca)

    paginator = Paginator(data, 30)
    page = request.GET.get('page', 1)
    ordens_de_servico = paginator.get_page(page)
    
    context={
        'titulo': apps.get_app_config('iluminacao').verbose_name,
        'ordens_de_servico': ordens_de_servico
    }
    return render(request, 'iluminacao/index.html', context)


@login_required
def add_os(request):
    
    form = OS_Form(initial={'tipo': Tipo_OS.objects.get(sigla='IP').id})

    if request.method=='POST':
        form=OS_Form(request.POST)
        if form.is_valid():
            os=form.save(commit=False)
            os.cadastrado_por=Pessoa.objects.get(user=request.user)
            os.save()

            return redirect('iluminacao:os_index')                

    context={
        'titulo': apps.get_app_config('iluminacao').verbose_name,
        'form': form,
    }

    return render(request, 'iluminacao/adicionar_os.html', context)


def detalhes_os(request, id):
    pessoa = Pessoa.objects.get(user=request.user)
    os = OrdemDeServico.objects.get(id=id)
    form_mensagem = NovaMensagemForm(initial={'os': os.id, 'pessoa': pessoa.id})
    try:
        os_ext=OS_ext.objects.get(os=os)        
    except:
        os_ext = None         
    if request.method=='POST': 
        form_mensagem=NovaMensagemForm(request.POST, request.FILES)
        if form_mensagem.is_valid():
           msg=form_mensagem.save(commit=False)
           msg.os=os
           msg.pessoa=pessoa
           msg.save()
           form_mensagem = NovaMensagemForm(initial={'os': os.id, 'pessoa': pessoa.id})       

    linha_tempo=OS_Linha_Tempo.objects.filter(os=os)
    context={
        'form_mensagem': form_mensagem,
        'linha_tempo': linha_tempo,
        'STATUS': STATUS_CHOICES,
        'PRIORIDADES': PRIORIDADE_CHOICES, 
        'titulo': apps.get_app_config('iluminacao').verbose_name,
        'os': os,
        'os_ext': os_ext
    }
    return render(request, 'iluminacao/detalhes_os.html', context)

@group_required('os_acesso', 'os_funcionario')
def change_status_os(request, id, opcao):
    os=OrdemDeServico.objects.get(id=id)
    os.status=opcao
    if opcao=='f':
        os.dt_conclusao=datetime.now()
    os.save()
    return redirect('iluminacao:detalhes_os', id=id)

@group_required('os_acesso', 'os_funcionario')
def change_prioridade_os(request, id, opcao):
    os=OrdemDeServico.objects.get(id=id)
    os.prioridade=opcao
    os.save()
    return redirect('iluminacao:detalhes_os', id=id)

@group_required('os_acesso', 'os_funcionario')
def atender_os(request, id):
    os=OrdemDeServico.objects.get(id=id)
    os.atendente=request.user
    os.save()
    return redirect('iluminacao:detalhes_os', id=id)

@group_required('os_acesso', 'os_funcionario')
def funcionarios_listar(request):
    funcionarios=Funcionario_OS.objects.all()
    context={
        'titulo': apps.get_app_config('iluminacao').verbose_name,
        'funcionarios': funcionarios
    }
    return render(request, 'equipe/funcionarios.html', context)

@group_required('os_acesso', 'os_funcionario')
def funcionario_cadastrar(request):
    if request.method=='POST':
        form=Funcionario_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    else:
        form=Funcionario_Form()
        context={
            'titulo': apps.get_app_config('iluminacao').verbose_name,
            'form': form
        }
    return render(request, 'equipe/funcionarios_cadastrar.html', context)

@group_required('os_acesso', 'os_funcionario')
def funcionario_editar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    form=Funcionario_Form(instance=funcionario)
    if request.method=='POST':
        form=Funcionario_Form(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    context={
        'titulo': apps.get_app_config('iluminacao').verbose_name,
        'form': form,
        'funcionario': funcionario
    }     
    return render(request, 'equipe/funcionarios_editar.html', context)

@group_required('os_acesso', 'os_funcionario')
def funcionario_deletar(request, id):
    funcionario=Funcionario.objects.get(id=id)
    funcionario.delete()

    return redirect('funcionarios')

@group_required('os_acesso', 'os_funcionario')
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
            return redirect('iluminacao:detalhes_os', id)
    context={
            'titulo': apps.get_app_config('iluminacao').verbose_name,   
            'form':form,
        }
    return render(request, 'iluminacao/adicionar_ext.html', context)

from django.db.models import Count

def imprimir_os(request, id):
    context={

    }
    return render(request, 'iluminacao/imprimir_os.html', context)

def graficos(request):
    pontos_por_bairro = OrdemDeServico.objects.values('bairro').annotate(total=Count('pontos_atendidos')).order_by('-total')
    os_por_bairro = OrdemDeServico.objects.values('bairro').annotate(total=Count('id')).order_by('-total')
    finalizados = OrdemDeServico.objects.filter(status='f').count()
    nao_finalizados = OrdemDeServico.objects.exclude(status='f').count()
    os_por_funcionario = Funcionario_OS.objects.annotate(total=Count('id')).order_by('-total')
    context = {
        'pontos_por_bairro': pontos_por_bairro,
        'os_por_bairro': os_por_bairro,
        'finalizados': finalizados,
        'nao_finalizados': nao_finalizados,
        'os_por_funcionario': os_por_funcionario,
    }
    return render(request, 'iluminacao/graficos.html', context)