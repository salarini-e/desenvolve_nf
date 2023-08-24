from django.shortcuts import render, redirect
from ..models import Empresa, Porte_da_Empresa, Ramo_de_Atuacao, Atividade
from ..forms import FormEmpresa, FormAlterarEmpresa
from django.contrib import messages
from autenticacao.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

@login_required()
@staff_member_required()
def sala_do_empreendedor_admin(request):
    context = {
        'titulo': 'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/admin/index.html', context)

@login_required()
@staff_member_required()
def mapeamento_empresa_e_fornecedores(request):
    empresas=Empresa.objects.all()
    if request.method == 'POST':
        if request.POST['cnpj']!='':
            empresas=empresas.filter(cnpj__icontains=request.POST['cnpj'])
        if request.POST['nome']!='':
            empresas=empresas.filter(nome__icontains=request.POST['nome'])
        if request.POST['porte']!='':
            empresas=empresas.filter(porte__porte__icontains=request.POST['porte'])
        if request.POST['atividade']!='':
            empresas=empresas.filter(atividade__atividade__icontains=request.POST['atividade'])
        if request.POST['ramo']!='':
            empresas=empresas.filter(ramo__ramo__icontains=request.POST['ramo'])
       
    paginator = Paginator(empresas, 100)
    context = {
        'titulo': 'Sala do Empreendedor',
        'portes': Porte_da_Empresa.objects.all(),
        'atividades': Atividade.objects.all(),
        'ramos': Ramo_de_Atuacao.objects.all(),
        'empresas': paginator.get_page(request.GET.get('page')),
        'paginator': paginator,
    }
    return render(request, 'sala_do_empreendedor/admin/mapeamento_empresa_e_fornecedores.html', context)