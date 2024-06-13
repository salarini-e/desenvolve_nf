from django.shortcuts import render, redirect
from .models import Curso
from .forms import LeadForm
from django.apps import apps
from django.contrib import messages
import asyncio

def index(request):
    context = {
        'titulo': apps.get_app_config('cursos_profissionais').verbose_name,
        'cursos': Curso.objects.all()
    }
    return render(request, 'cursos_profissionais/index.html', context)


def inscrever(request, id):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            
            # loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            # loop.run_until_complete(fazer_requisicao_post(url, data))
            return redirect(Curso.objects.get(id=id).link)
    else:
        form = LeadForm(initial={'curso': id})
    context = {
        'titulo': apps.get_app_config('cursos_profissionais').verbose_name,
        'curso': Curso.objects.get(id=id),
        'form': form
    }
    return render(request, 'cursos_profissionais/inscricao.html', context)

# def index(request):
#     try:
#         eventos = Evento.objects.filter(app_name='cursos', is_destaque = True)
#     except:
#         eventos=[]
    
#     cursos = list(Curso.objects.filter(tipo='C', ativo=True).order_by('?')[:9])
#     palestras = list(Curso.objects.filter(tipo='P', ativo=True).order_by('?')[:4])
#     shuffle(cursos)
#     context = { 
#         'titulo': apps.get_app_config('cursos_empresariais').verbose_name,
#         'eventos': eventos,
#         'cursos': cursos,   
#         'cursos_en': Curso_Ensino_Superior.objects.all()[:4],
#         'palestras': palestras 
#     }

#     return render(request, 'cursos_empresariais/index.html', context)
