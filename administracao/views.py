import json
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from cursos.models import *
from datetime import date, datetime
from django.template.loader import render_to_string

from .models import *
from cursos.forms import *


def enviar_email(aluno, turma):
    try:
        subject = f'Inscrição no curso {turma.curso.nome}'
        from_email = settings.EMAIL_HOST_USER
        to = [aluno.email]
        text_content = 'This is an important message.'
        html_content = render_to_string('email.html', {
            'turma': turma,
            'aluno': aluno
        }
        )
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as E:
        print(E)
    else:
        print('email enviado com sucesso!')


@login_required
def adm_cursos_criar(request):
    if request.user.is_superuser:
        form = CadastroCursoForm2(
            initial={'instituicao': 1, 'user_inclusao': request.user})
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])

        form = CadastroCursoForm(initial={
                                 'instituicao': 1, 'categoria': id_categoria, 'user_inclusao': request.user})
    if request.method == 'POST':
        form = CadastroCursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo curso cadastrado!')
            return redirect('adm_cursos_listar')

    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)


@login_required
def adm_cursos_editar(request, id):
    curso = Curso.objects.get(id=id)
    if request.user.is_superuser:
        form = CadastroCursoForm2(instance=curso)
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if curso.categoria == id_categoria:
            form = CadastroCursoForm(instance=curso)
        else:
            messages.error(
                request, 'Você não tem autorização para editar essa atividade.')
            return redirect('adm_cursos_listar')

    if request.method == 'POST':
        form = CadastroCursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'CADASTRAR': 'EDITAR',
        'curso': curso
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)


@login_required
def cadastrar_categoria(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_categoria_listar')
    form = CadastroCategoriaForm()
    if request.method == 'POST':
        form = CadastroCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova categoria cadastrada!')
            return redirect('adm_categorias_listar')
    context = {
        'form': form
    }
    return render(request, 'cursos/cadastrar_categoria.html', context)


@login_required
def cadastrar_local(request):
    form = CadastroLocalForm()
    if request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo local cadastrado!')
            return redirect('adm_locais_listar')
    context = {
        'form': form
    }
    return render(request, 'cursos/cadastrar_local.html', context)


@login_required
def administrativo(request):
    instrutor_aut = None

    try:
        instrutor_aut = Instrutor.objects.get(email=request.user.username)
    except:
        pass

    context = {
        'instrutor': False
    }
    if instrutor_aut and not request.user.is_superuser:
        context = {
            'instrutor': True
        }
    return render(request, 'administrativo.html', context)


@login_required
def turmas(request):
    return render(request, 'turmas/adm_turmas.html')


@login_required
def adm_turmas_criar(request):
    form = CadastroTurmaForm(
        initial={'instituicao': 1, 'user_inclusao': request.user})
    if request.method == 'POST':
        form = CadastroTurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova turma cadastrada com sucesso!')
            return redirect('adm_turmas_listar')
    context = {
        'form': form
    }
    return render(request, 'turmas/adm_turmas_criar.html', context)


@login_required
def adm_turmas_listar(request):
    instrutor_aut = None
    try:
        instrutor_aut = Instrutor.objects.get(email=request.user.username)
    except:
        pass
    if request.user.is_superuser:
        turmas = Turma.objects.all()
    elif instrutor_aut:
        turmas = Turma.objects.filter(instrutor=instrutor_aut)
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        turmas = Turma.objects.filter(curso__categoria=id_categoria)
    context = {
        'turmas': turmas
    }
    return render(request, 'turmas/adm_turmas_listar.html', context)


@login_required
def adm_cursos(request):
    return render(request, 'cursos/adm_cursos.html')


@login_required
def adm_cursos_listar(request):
    if request.user.is_superuser:
        cursos = Curso.objects.all()
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        cursos = Curso.objects.filter(categoria=id_categoria)
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/adm_cursos_listar.html', context)


@login_required
def adm_locais(request):
    return render(request, 'locais/adm_locais.html')


@login_required
def adm_locais_criar(request):
    form = CadastroLocalForm()
    if request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo local cadastrado!')
            return redirect('adm_locais_listar')

    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'locais/adm_locais_criar.html', context)


@login_required
def adm_locais_listar(request):
    locais = Local.objects.all()
    context = {
        'locais': locais
    }
    return render(request, 'locais/adm_locais_listar.html', context)


@login_required
def adm_locais_editar(request, id):
    local = Local.objects.get(id=id)
    form = CadastroLocalForm(instance=local)
    if request.method == 'POST':
        form = CadastroLocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Informações do local atualizada com sucesso')
            return redirect('adm_locais_listar')

    context = {
        'form': form,
        'local': local
    }
    return render(request, 'locais/adm_locais_editar.html', context)


@login_required
def adm_locais_excluir(request, id):
    local = Local.objects.get(id=id)
    local.delete()
    return redirect('adm_locais_listar')


@login_required
def adm_categorias(request):
    return render(request, 'categorias/adm_categorias.html')


@login_required
def adm_categorias_criar(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_categorias_listar')
    form = CadastroCategoriaForm()
    if request.method == 'POST':
        form = CadastroCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova categoria cadastrada!')
            return redirect('adm_categorias_listar')

    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'categorias/adm_categorias_criar.html', context)


@login_required
def adm_categorias_listar(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'categorias/adm_categorias_listar.html', context)


@login_required
def adm_categorias_excluir(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('adm_categorias_listar')


@login_required
def adm_categorias_editar(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CadastroCategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CadastroCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações da categoria atualizada!')
            return redirect('adm_categorias_listar')

    context = {
        'form': form,
        'categoria': categoria
    }
    return render(request, 'categorias/adm_categorias_editar.html', context)


@login_required
def adm_instituicoes_listar(request):
    instituicoes = Instituicao.objects.all()
    context = {
        'instituicoes': instituicoes
    }
    return render(request, 'instituicoes/adm_instituicoes_listar.html', context)


@login_required
def adm_instituicao_criar(request):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')
    form = Instituicao_form()
    if request.method == 'POST':
        form = Instituicao_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova instituição cadastrada!')
            return redirect('adm_instituicoes_listar')

    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'instituicoes/adm_instituicao_criar.html', context)


@login_required
def adm_turno_criar(request, id):

    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    turma = get_object_or_404(Turma, pk=id)
    form = Turno_form()

    if request.method == 'POST':
        form = Turno_form(request.POST)
        if form.is_valid():
            turno = form.save()

            Turno_estabelecido.objects.create(turno=turno, turma=turma)

            messages.success(request, 'Novo turno cadastrado!')
            return redirect('adm_turma_visualizar', turma.id)

    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'turno/adm_turno_criar.html', context)


@login_required
def adm_professores(request):
    context = {}
    return render(request, 'professores/adm_professores.html', context)


@login_required
def adm_professores_criar(request):
    form = CadastroProfessorForm()
    if request.method == 'POST':
        form = CadastroProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Instrutor cadastrada com sucesso!')
            return redirect('adm_professores')

    context = {
        'form': form,
    }
    return render(request, 'professores/adm_professores_criar.html', context)


@login_required
def adm_professores_listar(request):
    instrutores = Instrutor.objects.all()
    context = {
        'Instrutores': instrutores
    }
    return render(request, 'professores/adm_professores_listar.html', context)


@login_required
def adm_professores_editar(request, id):
    instrutor = Instrutor.objects.get(id=id)
    form = CadastroProfessorForm(instance=instrutor)
    if request.method == 'POST':
        form = CadastroProfessorForm(request.POST, instance=instrutor)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Informações do Instrutor atualizadas com sucesso!')
            return redirect('adm_professores')

    context = {
        'form': form,
        'instrutor': instrutor
    }
    return render(request, 'professores/adm_professores_editar.html', context)


@login_required
def adm_professores_excluir(request, id):
    instrutor = Instrutor.objects.get(id=id)
    instrutor.delete()
    return redirect('adm_professores')


@login_required
def adm_turmas_visualizar(request, id):
    turma = Turma.objects.get(id=id)
    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    matriculas = Matricula.objects.filter(turma=turma)

    matriculas_alunos = matriculas.filter(status='a').select_related('aluno')

    matriculas_selecionados = matriculas.filter(
        status='s').select_related('aluno')

    matriculas_candidatos = matriculas.filter(
        status='c').select_related('aluno')

    if request.method == 'POST':
        for i in request.POST.getlist("candidatos_selecionados"):
            if i != 'csrfmiddlewaretoken':
                matricula_candidato = Matricula.objects.get(pk=i)
                matricula_candidato.status = 's'
                matricula_candidato.save()

    context = {
        'turma': turma,
        'matriculas_alunos': matriculas_alunos,
        'matriculas_selecionados': matriculas_selecionados,
        'matriculas_candidatos': matriculas_candidatos,
        'qnt_alunos': len(matriculas_alunos)
    }

    return render(request, 'turmas/adm_turmas_editar.html', context)


@login_required
def visualizar_turma_editar(request, id):
    turma = Turma.objects.get(id=id)

    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    form = CadastroTurmaForm(instance=turma)
    if request.method == 'POST':
        form = CadastroTurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma editada com sucesso!')
            return redirect('adm_turma_visualizar', id)
    context = {
        'turma': turma,
        'form': form
    }
    return render(request, 'turmas/adm_turmas_editar_turma.html', context)


@login_required
def visualizar_turma_selecionado(request, matricula):
    matricula = Matricula.objects.get(pk=matricula)
    turma = Turma.objects.get(pk=matricula.turma_id)

    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    if turma.quantidade_permitido <= Matricula.objects.filter(turma=turma, status='a').count():
        messages.error(
            request, 'Turma cheia! Não é possível adicionar mais alunos.')
        return redirect('adm_turma_visualizar', id)

    birthDate = matricula.aluno.dt_nascimento
    today = date.today()
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))

    form = CadastroAlunoForm(instance=matricula.aluno, prefix='aluno')
    form_responsavel = ''

    if age < 18:
        responsavel = Responsavel.objects.get(aluno=matricula.aluno)
        form_responsavel = CadastroResponsavelForm(
            instance=responsavel, prefix='responsavel')

    if request.method == 'POST':
        form_aluno = CadastroAlunoForm(
            request.POST, instance=matricula.aluno, prefix='aluno')

        if form_aluno.is_valid():

            if form_responsavel != '':
                form_responsavel = CadastroResponsavelForm(
                    instance=responsavel, prefix='responsavel')
                if form_responsavel.is_valid():
                    form_responsavel.save()
                else:
                    raise Exception('Erro no form do responsável')

            aluno = form_aluno.save()
            matricula.status = 'a'
            matricula.save()

            messages.success = "Candidato selecionado cadastrado como aluno!"

        return redirect('adm_turma_visualizar', matricula.turma.id)

    context = {
        'form': form,
        'form_responsavel': form_responsavel,
        'turma': turma,
        'selecionado': matricula.aluno,
        'matricula': matricula
    }
    return render(request, 'turmas/adm_turmas_editar_selecionado.html', context)


@login_required
def excluir_turma(request, id):
    turma = Turma.objects.get(id=id)

    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    if request.user.is_superuser:
        turma.delete()

    return redirect('adm_turmas_listar')


@login_required
def adm_alunos_listar(request):
    if request.user.is_superuser:
        alunos = Aluno.objects.all()
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        alunos = Turma.objects.filter(curso__categoria=id_categoria)

    context = {
        'alunos': alunos
    }
    return render(request, 'alunos/adm_alunos_listar.html', context)


@login_required
def adm_aluno_visualizar(request, id):
    aluno = Aluno.objects.get(pk=id)

    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para acessar essa turma.')
        return redirect('administrativo')

    try:
        responsavel = Responsavel.objects.get(aluno=aluno)
        menor = True
    except:
        responsavel = ''
        menor = False

    context = {
        'aluno': aluno,
        'matriculas': Matricula.objects.filter(aluno=aluno).exclude(status='d'),
        'responsavel': responsavel,
        'menor': menor,
    }

    return render(request, 'alunos/adm_aluno_visualizar.html', context)


@login_required
def adm_aluno_editar(request, id):
    aluno = Aluno.objects.get(pk=id)

    form = CadastroAlunoForm(instance=aluno)
    if request.method == 'POST':
        form = CadastroAlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno(a) editado(a) com sucesso!')
            return redirect('adm_aluno_visualizar', id)

    context = {
        'aluno': aluno,
        'form': form
    }

    return render(request, 'alunos/adm_aluno_editar.html', context)


@login_required
def adm_aluno_excluir(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.user.is_superuser:
        aluno.delete()
        messages.success(request, 'Aluno excluido com sucesso')

    return redirect('adm_alunos_listar')


@login_required
def desmatricular_aluno(request, matricula):

    if request.user.is_superuser:
        matricula_obj = Matricula.objects.get(matricula=matricula)
        matricula_obj.status = 'd'
        matricula_obj.save()
        messages.success(request, 'Aluno desmatriculado com sucesso')

    else:
        messages.success(
            request, 'Por favor entre em contato com a administração do site para desmatricular um aluno')
        return redirect(request.META.get('HTTP_REFERER'))
    
    return redirect('adm_aluno_visualizar', matricula_obj.aluno.id)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@login_required
def adm_aula_criar(request, turma_id):
    if not request.user.is_superuser:
        messages.error(request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    turma = get_object_or_404(Turma, pk=turma_id)
    turno_choices = [(turno.id, turno) for turno in Turno_estabelecido.objects.filter(turma=turma)]
    form = Aula_form()
    form.fields['associacao_turma_turno'].choices = turno_choices

    if request.method == 'POST':
        form = Aula_form(data=request.POST)
        form.fields['associacao_turma_turno'].choices = turno_choices

        if form.is_valid():
            aula = form.save()
            messages.success(request, 'Aula registra!')
            return redirect('adm_aulas_listar', turma.id)

    context = {'form': form, 'CADASTRAR': 'NOVO'}
    return render(request, 'aulas/adm_aula_criar.html', context)


@login_required
def adm_aulas_listar(request, turma_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    turma = get_object_or_404(Turma, pk=turma_id)
    aulas = Aula.objects.filter(associacao_turma_turno__turma=turma)

    context = {
        'turma': turma,
        'aulas': aulas
    }

    return render(request, 'aulas/adm_aulas_listar.html', context)


@login_required
def adm_aula_visualizar(request, turma_id, aula_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    if request.method == "POST":
        acao = request.POST.get('acao') or 'p'
        for matricula in request.POST.getlist('alunos_selecionados'):
            presenca = Presenca.objects.get_or_create(matricula=Matricula.objects.get(matricula=matricula), aula_id=aula_id)[0]
            presenca.status = acao
            presenca.save()

    turma = get_object_or_404(Turma, pk=turma_id)
    aula = get_object_or_404(Aula, pk=aula_id)
    matriculas = Matricula.objects.filter(turma=turma)

    matriculados = []
    for matricula in matriculas:
        try:
            presenca = Presenca.objects.get(aula=aula, matricula=matricula)
        except:
            presenca = ''

        matriculados.append( {'matricula': matricula, 'presenca': presenca} )

    context = {
        'turma': turma,
        'matriculados': matriculados,
        'aula': aula,
    }

    return render(request, 'aulas/adm_aula_visualizar.html', context)

@login_required
def adm_justificativa_criar(request, presenca_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    form = Justificativa_form()
    presenca = get_object_or_404(Presenca, pk=presenca_id)

    if request.method == "POST":
        form = Justificativa_form(request.POST)
        if form.is_valid():
            justificativa = form.save()
            presenca.justificativa = justificativa
            presenca.save()

            messages.error(request, 'Justificativa registrada!')
            return redirect('adm_aula_visualizar', presenca.aula.associacao_turma_turno.turma.id, presenca.aula.id)
    
    context = {
        'presenca': presenca,
        'form': form
    }

    return render(request, 'justificativas/adm_justificativa_criar.html', context)

@login_required
def adm_justificativa_visualizar(request, presenca_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para criar uma nova categoria.')
        return redirect('adm_instituicoes_listar')

    presenca = get_object_or_404(Presenca, pk=presenca_id)

    context = {
        'presenca': presenca,
        'aluno': presenca.matricula.aluno
    }

    return render(request, 'justificativas/adm_justificativa_visualizar.html', context)