from django.shortcuts import render, redirect
from django.apps import apps
from eventos.models import Evento
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from autenticacao.models import Pessoa
from django.utils import timezone

def index(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'eventos': Evento.objects.filter(app_name='financas')
    }
    return render(request, 'financas/index.html', context)


def formularios(request):
    arquivos = {'alvara': [['Requerimento Alvará', 'alvara/REQUERIMENTO-DE-ALVARA.pdf'],
                           ['Requerimento de Baixa de Débito',
                           'alvara/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                           ['Requerimento de Certidão de ISS e Alvará', 'alvara/ REQUERIMENTO-DE-CERTIDAO-DE-ISS-E-ALVARA-1-4-1.pdf'], ['Requerimento de Revisão de Taxa de Alvará', 'REQUERIMENTO-DE-REVISAO-DE-TAXA-DE-ALVARA-1.pdf']],
                'certidao': [['Requerimento de Averbação de Escritura',
                              'certidoes/REQUERIMENTO-DE-AVERBACAO-DE-ESCRITURA.pdf'],
                             ['Requerimento de Certidão', 'certidoes/REQUERIMENTO-DE-CERTIDAO-1.pdf']],
                'iptu': [['Autorizacao para Vistoria Predial', 'certidoes/AUTORIZACAO-VISTORIA-PREDIAL-3.pdf'],
                         ['Requerimento de Baixa de Débito', 'iptu/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                         ['Requerimento de Inclusao de Possuidor', 'iptu/REQUERIMENTO-DE-INCLUSAO-DE-POSSUIDOR.pdf'],
                         ['requerimento_recolhimento', 'iptu/REQUERIMENTO-DE-RECOLHIMENTO-DE-TRIBUTOS-1.pdf'],
                         ['requerimento_revisao', 'iptu/REQUERIMENTO-REVISAO-DE-IPTU-1.pdf']],
                'itbi': [['Declaração Ciencia ITBI', 'itbi/DECLARACAO-DE-CIENCIA-DE-ITBI.pdf'],
                         ['Declaração Transacao Imobiliaria', 'itbi/Declaracao-de-Transacao-Imo-biliaria-ITBI-PMNF-5.pdf'],
                         ['Requerimento Revisao ITBI', 'itbi/REQUERIMENTO-DE-REVISAO-DE-ITBI.pdf']],
                'isencao': [['Requerimento Imunidade Tributaria', 'isencao/REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf'],
                            ['Requerimento Isenção',
                             'isencao/REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf'],
                            ['Requerimento Insencao Não Incidência Tributaria', 'isencao/REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf'], ['Requerimento Isenção Parcial Tombamento', 'isencao/REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf']],
                'diversos': [['Declaração de Residência', 'diversos/DECLARACAO-DE-RESIDENCIA.pdf'],
        ['Requerimento de Adesão',
         'diversos/REQUERIMENTO-DE-ADESAO.pdf'],
        ['Requerimento de Atualização Cadastral',
         'diversos/REQUERIMENTO-DE-ATUALIZACAO-CADASTRAL-1.pdf'],
       
    ]}
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'arquivos': arquivos,
    }
    return render(request, 'financas/formularios.html', context)

def legislacao(request):
    return render(request, 'financas/legislacao.html')

def administracao(request):
    return render(request, 'financas/admin.html')

@login_required
def add_conselheiro(request):
    if request.method == 'POST':
        form = ConselheirosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conselheiro adicionado com sucesso!')
            return redirect('financas:index')
    else:
        form = ConselheirosForm(initial={'ativo': True, 'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar Conselheiro',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar um novo conselheiro',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)

@login_required
def add_pauta(request):
    if request.method == 'POST':
        form = Pauta_de_JulgamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pauta de Julgamento adicionada com sucesso!')
            return redirect('financas:index')
    else:
        form = Pauta_de_JulgamentoForm(initial={'ativo': True, 'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar Pauta de Julgamento',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar uma nova pauta de julgamento',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)

@login_required
def add_sumula(request):
    if request.method == 'POST':
        form = SumulasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sumula adicionada com sucesso!')
            return redirect('financas:index')
    else:
        form = SumulasForm(initial={'ativo': True, 'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar Sumula',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar uma nova sumula',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)


@login_required
def add_acordao(request):
    if request.method == 'POST':
        form = AcordaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Acórdão adicionado com sucesso!')
            return redirect('financas:index')
        else:
            messages.error(request, 'Erro ao adicionar acórdão. Por favor, verifique os campos.')
    else:
        form = AcordaoForm(initial={'ativo': True, 'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar Acórdão',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar um novo acórdão',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)

@login_required
def add_ata(request):
    if request.method == 'POST':
        form = AtaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ata adicionada com sucesso!')
            return redirect('financas:index')
        else:
            messages.error(request, 'Erro ao adicionar ata. Por favor, tente novamente.')
    else:
        form = AtaForm(initial={'ativo': True, 'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar ata',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar um nova ata da reunião',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)

@login_required
def add_voto_relator(request):
    if request.method == 'POST':
        form = Voto_RelatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voto relator adicionada com sucesso!')
            return redirect('financas:index')
        else:
            messages.error(request, 'Erro ao adicionar votor do relator. Por favor, tente novamente.')
    else:
        form = Voto_RelatorForm(initial={'user_inclusao': request.user})
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'titulo_form': 'Adicionar voto do relator',
        'subtitulo_form': 'Preencha os campos abaixo para adicionar um novo voto de relator',
        'texto_form': '',
        'form': form
    }
    return render(request, 'financas/forms.html', context)


def conselho(request):
    conselheiros = Conselheiros.objects.filter(ativo=True)
    datas = Data_Reunião.objects.filter(data__gte=timezone.now()).order_by('-data')
    pautas = Pauta_de_Julgamento.objects.filter(ativo=True).order_by('-data')
    sumulas = Sumulas.objects.filter(ativo=True).order_by('-id')
    acordao = Acordao.objects.filter(ativo=True).order_by('-id')
    atas = Ata.objects.filter(ativo=True).order_by('-id')
    votos = Voto_Relator.objects.all().order_by('-id')
    context = {
                'titulo': apps.get_app_config('financas').verbose_name,
                'datas': datas,
                'pautas': pautas,
                'sumulas': sumulas,
                'acordaos': acordao,
                'conselheiro': conselheiros,
                'atas': atas,
                'votos': votos
        }
    if request.user.is_authenticated:
        pessoa = Pessoa.objects.get(user=request.user)
        if conselheiros.filter(cpf=pessoa.cpf).exists():
            context['conselheiro']=True
            if conselheiros.get(cpf=pessoa.cpf).admin:
                context['admin']=True
            else:
                context['admin']=False
        
        else:
            context['conselheiro']=False
            context['admin']=False
    
    return render(request, 'financas/conselho.html', context)