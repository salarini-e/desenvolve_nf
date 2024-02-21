from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from autenticacao.models import Pessoa
from .forms import *
from .api import ApiProtocolo
from django.contrib import messages
from django.http import HttpResponse
from .functions import send_email_for_process
def index(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        # 'vagas': Locais_de_Estagio.objects.all()[:8]
    }
    return render(request, 'estagio/index.html', context)

def vagas(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'vagas': Vagas.objects.all()
    }
    return render(request, 'estagio/vagas.html', context)

def listar_instituicoes(request):
    instituicoes = Universidade.objects.filter(ativa=True)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'vagas': Vagas.objects.all(),
        'instituicoes': instituicoes
    }
    return render(request, 'estagio/listar_instituicoes.html', context)

def listar_cursos_e_locais(request, id):
    instituicao = Universidade.objects.get(id=id)
    cursos = Curso.objects.filter(universidade__id=instituicao.id)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'instituicao': instituicao,
        'cursos': cursos,
    }
    return render(request, 'estagio/listar_cursos_e_locais.html', context)

@staff_member_required
def locais_detalhes(request, id, id_local):
    local=Locais_de_Estagio.objects.get(id=id_local)
    context = {
        'local': local,
        'id': id
    }
    return render(request, 'estagio/secretaria_locais_detalhes.html', context)

@staff_member_required
def locais_detalhes_adicionar_ou_remover(request, id, id_local):
    local=Locais_de_Estagio.objects.get(id=id_local)
    if request.method == 'POST':
        form=Form_locais_adicionar_ou_remover_cursos(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('estagio:listar_detalhes_do_local', id, id_local)    
    form=Form_locais_adicionar_ou_remover_cursos(instance=local)
    context = {
        'local': local,
        'id': id,
        'form': form
    }
    return render(request, 'estagio/secretaria_locais_detalhes_adicionar_ou_remover.html', context)
    
def getVagas(request, id):    
    #api locais
    vagas = Vagas.objects.filter(curso__id=id)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'vagas': vagas,
    }
    return render(request, 'estagio/getVagas.html', context)
 
def getLocais(request, id):    
    #api locais
    vaga = Locais_de_Estagio.objects.filter(cursos__id=id)
    # print(vaga)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'vaga': vaga,
        'id': id
    }
    return render(request, 'estagio/getLocais.html', context)

@login_required
def area_do_estudante(request):
    try:
        estudante=Estudante.objects.filter(pessoa=Pessoa.objects.get(user=request.user)).last()
        print(estudante)
        estudante_vagas=Estudante_Vaga.objects.filter(estudante=estudante).order_by('-id')
        print(estudante_vagas)
    except Exception as e:
        print(e)
        estudante=False
        estudante_vagas=False
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        # 'vagas': Vagas.objects.all(),
        'estudante': estudante,
        'estudante_vagas': estudante_vagas
    }
    return render(request, 'estagio/area_do_estudante.html', context)

@login_required
def area_da_universidade(request):
    try: 
        responsavel=Responsavel_Universidade.objects.get(pessoa=Pessoa.objects.get(user=request.user))
        print(responsavel)
        estudante_vagas=Estudante_Vaga.objects.filter(vaga__curso__universidade=responsavel.universidade)
    except:
        responsavel=[]   
        print(request.user.is_superuser)     
        if request.user.is_superuser:
            estudante_vagas=Estudante_Vaga.objects.all()
        else:
            return redirect('/')
    
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        # 'vagas': Vagas.objects.filter(),
        'estudante': responsavel,
        'estudante_vagas': estudante_vagas.order_by('-id')
    }
    return render(request, 'estagio/area_da_universidade.html', context)

@login_required
def processo_da_vaga(request, id):
    estudante_vaga=Estudante_Vaga.objects.get(id=id) 
    processo=Processo.objects.get(estudante_vaga=estudante_vaga.id)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'processo': processo,
        'historico': Historico_Processo.objects.filter(processo=processo).order_by('-id'),
        'id': id,
    }
    return render(request, 'estagio/processo_da_vaga.html', context)

@login_required
def adm_processo_da_vaga(request, id):
    estudante_vaga=Estudante_Vaga.objects.get(id=id) 
    processo=Processo.objects.get(estudante_vaga=estudante_vaga.id)
    if estudante_vaga.TCE:
        tce=estudante_vaga.TCE.url
    else:
        tce=False
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'processo': processo,
        'estudante': estudante_vaga.estudante,
        'historico': Historico_Processo.objects.filter(processo=processo).order_by('-id'),
        'back_to': request.GET.get('next'),
        'id': id, 
        'TCE': tce

    }
    return render(request, 'estagio/adm_processo_da_vaga.html', context)

@login_required
def anexar_tce(request, id):
    estudante_vaga=Estudante_Vaga.objects.get(id=id)
    if request.method == 'POST':
        forms = Estudante_TCE_form(request.POST, request.FILES, instance=estudante_vaga)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'TCE enviado com sucesso!')
    context={
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'form': Estudante_TCE_form(instance=estudante_vaga),
        'id': id,
        'url': estudante_vaga.TCE.url if estudante_vaga.TCE else False
        
    }
    return render(request, 'estagio/anexar_tce.html', context)

@login_required
def visualizar_tce(request, id):
    estudante_vaga=Estudante_Vaga.objects.get(id=id)
    context={
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'form': False,
        'id': id,
        'url': estudante_vaga.TCE.url if estudante_vaga.TCE else False
        
    }
    return render(request, 'estagio/anexar_tce.html', context)
    
@login_required
def adm(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
    }
    return render(request, 'estagio/adm.html', context)

@login_required
def listar_candidato(request):
    candidatos=Estudante_Vaga.objects.filter(status=0)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'subtitulo': 'candidatos',
        'estudante': candidatos.order_by('-data_inclusao'),
        'total': candidatos.count()
    }
    return render(request, 'estagio/listar_candidatos.html', context)

@login_required
def listar_estagiario(request):
    candidatos=Estudante_Vaga.objects.filter(status=1)
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'subtitulo': 'estagiários',
        'estudante': candidatos,
        'total': candidatos.count(),
        'supervisor': True
    }
    return render(request, 'estagio/listar_estagiarios.html', context)

def getCursos(request, id):
    cursos = Curso.objects.filter(universidade__id=id)
    print(cursos)
    context = {
        'cursos': cursos,
    } 
    return render(request, 'estagio/getCursos.html', context)

from django.http import JsonResponse
def get_courses_by_university(request, university_id):
    print("university_id:", university_id)  # Adicione esta linha para depurar
    courses = Curso.objects.filter(universidade_id=university_id).values('id', 'nome')
    print("courses:", list(courses))  # Adicione esta linha para depurar
    return JsonResponse(list(courses), safe=False)

@login_required
def candidatar_se_vaga(request, id, id_curso):
    pessoa = Pessoa.objects.get(user=request.user)
    curso = Curso.objects.get(id=id_curso)
    try:
        instance=Estudante.objects.get(pessoa=pessoa)
        forms_estudante = Estudante_form(instance=instance, initial={'universidade': instance.universidade.id, 'curso': instance.curso.id})
    except:
        instance=False
        forms_estudante = Estudante_form(initial={'pessoa': pessoa.id, 'universidade': curso.universidade.id, 'curso': curso.id})

    local =  Locais_de_Estagio.objects.get(id=id)
    # print(local)
    # print(local.cursos.all)
    forms_vaga = Estudante_vaga_form(initial={'status': 0, 'local_do_estagio_de_pretensao': id})

    if request.method == 'POST':
        if instance:
             forms_estudante = Estudante_form(request.POST, instance=instance)
        else:
            forms_estudante = Estudante_form(request.POST)

        forms_vaga = Estudante_vaga_form(request.POST)
        # print(request.POST)
        if forms_estudante.is_valid():
            estudante=forms_estudante.save()
            estudante.pessoa=pessoa
            estudante.save()
            # print('curso:', estudante.curso)
            if  forms_vaga.is_valid(estudante):
                estudante_vaga=forms_vaga.save(commit=False)
                estudante_vaga.estudante=estudante
                estudante_vaga.status='0'
                # estudante_vaga.vaga=vaga
                estudante_vaga.universidade=estudante.universidade
                estudante_vaga.matricula=estudante.matricula
                estudante_vaga.save()
                start_processo=Processo(estudante_vaga=estudante_vaga)
                start_processo.save()
                start_historico=Historico_Processo(status=0, processo=start_processo, mensagem='')
                start_historico.save()
                # parametros = {
                #     'numeroDocumentoJuridico': estudante.pessoa.cpf,
                #     # 'numeroProcesso': '2023',
                #     'anoProcesso': '2023',
                #     'dataProcesso': '2023-08-04 16:24:04',
                #     'resumoEcm': 'Testando API 2'
                # }
                # api = ApiProtocolo.cadastrarProcesso(parametros)
                messages.success(request, 'Candidatura realizada com sucesso!')
                return redirect('estagio:area_do_estudante')
    context = {
        'forms_estudante': forms_estudante,
        'forms_vaga': forms_vaga,
        'local': local,
        'curso': curso
    }
    return render(request, 'estagio/candidatar_se_vaga.html', context)

def editar_estudante(request, id):
    instance = Estudante_Vaga.objects.get(id=id)
    forms = Editar_estudante_forms(instance=instance)
    if request.method == 'POST':
        forms = Editar_estudante_forms(request.POST, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('estagio:editar_candidato_processo', id)
    context = {
        'forms':forms
    }
    return render(request, 'estagio/editar_estudante.html', context)

def editar_estudante_processo(request, id):
    instance = Estudante_Vaga.objects.get(id=id)    
    processo=Processo.objects.get(estudante_vaga=instance)
    try:
        historico_anterior=Historico_Processo.objects.get(processo=processo)
    except:
        historico_anterior='0'
    forms=Historico_processo_estudante_forms(initial={'statuts': historico_anterior, 'processo': processo.id})
    if request.method == 'POST':
        forms=Historico_processo_estudante_forms(request.POST)
        if forms.is_valid():
            historico=forms.save()
            resp=send_email_for_process(instance, historico)
            if resp == 'Falha ao enviar email.':
                messages.warning(request, 'Email não enviado, verifique o email do estudante')
            else:
                messages.success(request, 'Um email foi enviado para o estudante!')
            return redirect('estagio:adm_processo_da_vaga', id)

            
    context = {
        'forms':forms
    }
    return render(request, 'estagio/criar_processo_estudante.html', context)

def cadastro_vaga(resquest):
    forms = Cadatrar_Vaga_form()
    if resquest.method == 'POST':
        forms = Cadatrar_Vaga_form(resquest.POST, resquest.FILES)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms,
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
    }
    return render(resquest, 'estagio/cadastrar_vagas.html', context)

def cadastrar_universidade(request):
    forms = Universidade_form()
    if request.method == 'POST':
        forms = Universidade_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms,
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
    }
    return render(request, 'estagio/cadastrar_universidade.html', context)

def listar_universidade(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'universidades': Universidade.objects.all(),
    }
    return render(request, 'estagio/universidade.html', context)

def cadastrar_curso(request, id):
    forms = Curso_form(initial={
        'universidade':id,
    })
    if request.method == 'POST':
        # Valida o id no form se n vai dar merda
        forms = Curso_form(request.POST)
        if forms.is_valid():
            curso = forms.save()
            curso.universidade = Universidade.objects.get(id=id)
            curso.save()
            return redirect('estagio:curso', id)
    context={
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'forms':forms,
        'id': id
    }
    return render(request, 'estagio/cadastrar_curso.html', context)

def cadastrar_universidade_local(request, id):
    forms = Universidade_local_form(secretaria=id)
    if request.method == 'POST':
        forms = Universidade_local_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms,
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
    }
    return render(request, 'estagio/cadastrar_universidade.html', context)

def listar_curso(request, id):
    context = {
        'universidade': Universidade.objects.get(id=id),
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'cursos':Curso.objects.filter(universidade__id=id),
        'id': id
    }
    return render(request, 'estagio/cursos.html', context)

def editar_curso(request, id):
    instance = Curso.objects.get(id=id)
    forms = Editar_Curso_forms(instance=instance)
    if request.method == 'POST':
        forms = Editar_Curso_forms(request.POST, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('estagio:curso', id)
    context = {
        'forms':forms,
        'id': id
    }
    return render(request, 'estagio/editar_curso.html', context)

def listar_supervisor(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'supervisores':Supervisor.objects.all(),
    }
    return render(request, 'estagio/supervisor.html', context)

def cadastrar_supervisor(request):
    forms = Supervisor_form()
    if request.method == 'POST':
        forms = Supervisor_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms
    }
    return render(request, 'estagio/cadastrar_supervisor.html', context)

def editar_supervisor(request, id):
    instance = Supervisor.objects.get(id=id)
    forms = Editar_Supervisor_forms(instance=instance)
    if request.method == 'POST':
        forms = Editar_Supervisor_forms(request.POST, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('estagio:listar_supervisor')
    context = {
        'forms':forms
    }
    return render(request, 'estagio/editar_supervisor.html', context)

def listar_secretaria(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'secretarias':Secretaria.objects.all(),
    }
    return render(request, 'estagio/secretaria.html', context)

def listar_vagas(request):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'vagas': Vagas.objects.all(),
        
    }
    return render(request, 'estagio/listar_vagas.html', context)

def cadastrar_vagas(request):
    forms = Cadatrar_Vaga_form()
    if request.method == 'POST':
        forms = Cadatrar_Vaga_form(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('estagio:listar_vagas')
    context = {
        'forms':forms
    }
    return render(request, 'estagio/cadastrar_vagas.html', context)

def editar_vagas(request, id):
    instance = Vagas.objects.get(id=id)
    forms = Editar_Vaga_form(instance=instance)
    if request.method == 'POST':
        forms = Editar_Vaga_form(request.POST, request.FILES, instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect('estagio:listar_vagas')
    context = {
        'forms':forms
    }
    return render(request, 'estagio/editar_vagas.html', context)

def listar_secretaria_locais(request, id):
    context = {
        'titulo':'Programa de Desenvolvimento de Estágio de Estudante',
        'secretaria': Secretaria.objects.get(id=id),
        'locais': Locais_de_Estagio.objects.filter(secretaria__id=id),
        'id':id
    }
    return render(request, 'estagio/secretaria_locais.html', context)

def cadastrar_secretaria(request):
    forms = Secretaria_form()
    if request.method == 'POST':
        forms = Secretaria_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms':forms
    }
    return render(request, 'estagio/cadastrar_secretaria.html', context)

def cadastrar_local(request,id):
    forms = Local_form(initial={'secretaria':id})
    if request.method == 'POST':
        forms = Local_form(request.POST)
        if forms.is_valid():
            local = forms.save()
            local.secretaria = Secretaria.objects.get(id=id)
            local.save()
            return redirect('estagio:listar_secretaria_locais', id)
    context = {
        'forms':forms,
        'id':id
    }
    return render(request, 'estagio/cadastrar_local.html', context)