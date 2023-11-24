from django.shortcuts import render, redirect
from ..models import Empresa
from ..forms import FormEmpresa, FormAlterarEmpresa
from django.contrib import messages
from autenticacao.models import Pessoa
from django.contrib.auth.decorators import login_required

@login_required()
def minha_empresa(request):
    empresas=Empresa.objects.filter(user_register=request.user)
    context = {
        'titulo': 'Sala do Empreendedor - Minha Empresa',
        'empresas': empresas
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/index.html', context)

import re
@login_required()
def cadastrar_empresa(request):
    form=FormEmpresa()
    if request.method == 'POST':
        form = FormEmpresa(request.POST)
        if form.is_valid():
            empresa=form.save()
            empresa.user_register=request.user
            empresa.cnpj=re.sub(r'[^0-9]', '', empresa.cnpj)
            empresa.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            pessoa=Pessoa.objects.get(user=request.user)
            pessoa.possui_cnpj=True
            pessoa.save()
            return redirect('empreendedor:minha_empresa')
    context = {
        'titulo': 'Sala do Empreendedor - Cadastrar Empresa',
        'form': form
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/cadastro_empresa.html', context)

@login_required()
def editar_empresa(request, id):
    instance=Empresa.objects.get(id=id)
    
    if request.user.is_staff or request.user==instance.user_register:
    
        form=FormAlterarEmpresa(instance=instance)
        if request.method == 'POST':
            form = FormAlterarEmpresa(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Informações da empresa atualizada com sucesso!')
                return redirect('empreendedor:minha_empresa')
        context = {
            'empresa': instance,
            'titulo': 'Sala do Empreendedor - Editar Empresa',
            'form': form
        }
        return render(request, 'sala_do_empreendedor/minha-empresa/editar_empresa.html', context)
    return redirect('empreendedor:minha_empresa')
