from django.shortcuts import render, redirect
from ..models import Empresa
from ..forms import FormEmpresa
from django.contrib import messages
from autenticacao.models import Pessoa

def minha_empresa(request):
    empresas=Empresa.objects.filter(user_register=request.user)
    context = {
        'titulo': 'Sala do Empreendedor',
        'empresas': empresas
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/index.html', context)

def cadastrar_empresa(request):
    form=FormEmpresa()
    if request.method == 'POST':
        form = FormEmpresa(request.POST)
        if form.is_valid():
            empresa=form.save()
            empresa.user_register=request.user
            empresa.save()
            messages.success(request, 'Empresa cadastrada com sucesso! Aguarde a aprovação da Sala do Empreendedor.')
            pessoa=Pessoa.objects.get(user=request.user)
            pessoa.possui_cnpj=True
            pessoa.save()
            return redirect('empreendedor:minha_empresa')
    context = {
        'titulo': 'Sala do Empreendedor',
        'form': form
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/cadastro_empresa.html', context)
