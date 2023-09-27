from django.shortcuts import render, redirect
from ..models import Empresa, Porte_da_Empresa, Ramo_de_Atuacao, Atividade, Andamento_Processo_Digital, Status_do_processo, Processo_Digital, Processo_Status_Documentos_Anexos
from ..forms import FormEmpresa, FormAlterarEmpresa, Criar_Processo_Form, Criar_Andamento_Processo
from django.contrib import messages
from autenticacao.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

@login_required()
@staff_member_required()
def sala_do_empreendedor_admin(request):
    context = {
        'titulo': 'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/admin/index.html', context)

@login_required()
@staff_member_required()
def processos_digitais_admin(request):
    proecsesos = Processo_Digital.objects.all().order_by('-dt_solicitacao')    
    paginator = Paginator(proecsesos, 50)
    context = {
        'titulo': 'Sala do Empreendedor',
        'processos': paginator.get_page(request.GET.get('page')),
    }
    return render(request, 'sala_do_empreendedor/admin/processos_digitais/index.html', context)

import re
@login_required()
@staff_member_required()
def requerimento_iss_admin(request):
    if request.method == 'POST':
        form = Criar_Processo_Form(request.POST, request.FILES)
        try:
            pessoa = Pessoa.objects.get(cpf=re.sub(r'[^0-9]', '', request.POST['cpf']))
        except:
            pessoa = None
        print(pessoa)
        if pessoa:            
            if form.is_valid():
                processo = form.save(commit=False)
                processo.tipo_processo = '0'
                processo.solicitante = pessoa.user
                processo.save()
                andamento = Andamento_Processo_Digital(
                    processo=processo,              
                    status=Status_do_processo.objects.get(id=1),                     
                    observacao = 'Processo criado pelo servidor. Aguardando avaliação do pedido.',
                    servidor = request.user 
                )
                andamento.save()
                status_documentos = Processo_Status_Documentos_Anexos(
                    processo=processo,
                    rg_status = '0',
                    comprovante_endereco_status = '0',
                    diploma_ou_certificado_status = '0',
                    licenca_sanitaria = '0',
                    espelho_iptu_status = '0'
                    
                )
                status_documentos.save()
                messages.success(request, 'Processo criado com sucesso!')
                return redirect('empreendedor:processos_digitais_admin')
        else:
            messages.error(request, 'Não foi encontrado usuário com esse CPF!')
    else:
        form = Criar_Processo_Form(initial={'tipo_processo': '0', 'solicitante': request.user.id})
        
    context = {
        'titulo': 'Sala do Empreendedor',
        'form': form
    }
    return render(request, 'sala_do_empreendedor/admin/processos_digitais/cadastro_processo.html', context)

@login_required()
@staff_member_required()
def andamento_processo(request, id):
    processo = Processo_Digital.objects.get(id=id)
    andamentos = Andamento_Processo_Digital.objects.filter(processo=processo).order_by('-id')
    status_documentos = Processo_Status_Documentos_Anexos.objects.get(processo=processo)
    context = {
        'titulo': 'Sala do Empreendedor',
        'processo': processo,
        'andamentos': andamentos,
        'status_documentos': status_documentos
        
    }
    return render(request, 'sala_do_empreendedor/admin/processos_digitais/andamento_processo.html', context)

@login_required()
@staff_member_required()
def mudaStatusRG(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        status_documentos = Processo_Status_Documentos_Anexos.objects.get(id=id)
        status_documentos.rg_status = data.get('status')
        status_documentos.save()
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})

@login_required()
@staff_member_required()
def mudaStatusComprovante(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        status_documentos = Processo_Status_Documentos_Anexos.objects.get(id=id)
        status_documentos.comprovante_endereco_status = data.get('status')
        status_documentos.save()
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})

@login_required()
@staff_member_required()
def mudaStatusCertificado(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        status_documentos = Processo_Status_Documentos_Anexos.objects.get(id=id)
        status_documentos.diploma_ou_certificado_status = data.get('status')
        status_documentos.save()
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})

@login_required()
@staff_member_required()
def mudaStatusLicenca(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        status_documentos = Processo_Status_Documentos_Anexos.objects.get(id=id)
        status_documentos.licenca_sanitaria= data.get('status')
        status_documentos.save()
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})

@login_required()
@staff_member_required()
def mudaStatusEspelho(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id')
        status_documentos = Processo_Status_Documentos_Anexos.objects.get(id=id)
        status_documentos.espelho_iptu_status = data.get('status')
        status_documentos.save()
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})

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