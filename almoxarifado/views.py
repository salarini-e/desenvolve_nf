import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator

from .models import *
from .forms import *

def index(request):
    data = Material.objects.all()
    paginator = Paginator(data, 30)
    page = request.GET.get('page', 1)
    materiais = paginator.get_page(page)

    context = {
        'materiais': materiais
    }
    return render(request, 'almoxarifado/index.html', context)


def listar_tipo_materiais(request):
    context = {
        'tipos': Tipo_Material.objects.all()
    }
    return render(request, 'almoxarifado/listar_tipo_materiais.html', context)


def adicionar_tipo_materiais(request):
    if request.method == 'POST':
        form = Tipo_Material_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de material cadastrado!')
            return redirect('alm_listar_tipos')
    else:
        form = Tipo_Material_Form()

    context = {
        'form': form
    }
    return render(request, 'almoxarifado/adicionar_tipo_materiais.html', context)


def adicionar_material(request, tipo):
    tipo = Tipo_Material.objects.get(id=tipo)

    if request.method == 'POST':
        form = Material_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado!')
            return redirect('alm_listar_tipos')
    else:
        form = Material_Form(initial={'tipo': tipo.id})

    context = {
        'form': form
    }
    return render(request, 'almoxarifado/adicionar_novo_material.html', context)


def adicionar_material_ao_estoque(request):
    if request.method == 'POST':
        form = Log_estoque_Form(request.POST)
        form_tipo = Exibir_Tipo_Material_Form(request.POST)
        if form.is_valid():
            log = form.save()
            material = Material.objects.get(id=log.material.id)
            log.qnt_em_estoque = material.qnt_em_estoque
            material.qnt_em_estoque = material.qnt_em_estoque+log.add_quantidade
            material.save()
            log.save()
            if log.add_quantidade == 1:
                messages.success(request, f"{log.add_quantidade} nova unidade adicionada ao estoque. Total: {material.qnt_em_estoque}.")
            else: 
                messages.success(request, f"{log.add_quantidade} novas unidades adicionadas ao estoque. Total: {material.qnt_em_estoque}.")
            return redirect('alm_index')
    else:
        form = Log_estoque_Form()
        form_tipo = Exibir_Tipo_Material_Form()

    context = {
        'form': form,
        'form_tipo': form_tipo
    }
    return render(request, 'almoxarifado/adicionar_material_ao_estoque.html', context)


@login_required
def listar_materiais(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        if not data['tipo']:
            return Exception("DEU MERDA, CADE O ID????")
        return JsonResponse({'data': list(Material.objects.filter(tipo=data['tipo']).values())})
    else:
        raise PermissionDenied()

