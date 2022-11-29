import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
import json
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .models import Aluno, Candidato, Categoria, Curso, Matricula, Instrutor, Responsavel, Turma, Local
from .forms import CadastroAlunoForm, CadastroCandidatoForm, CadastroCursoForm, CadastroCategoriaForm, CadastroCursoForm2, CadastroLocalForm, CadastroProfessorForm, CadastroResponsavelForm, CadastroTurmaForm

from datetime import date, datetime


def index(request):
    return render(request, 'cursos/index.html')


def cursos(request):
    form = CadastroCandidatoForm()
    categorias = Categoria.objects.all()
    cursos = []
    for i in categorias:
        cursos.append(
            {'categoria': i, 'curso': Curso.objects.filter(categoria=i, ativo=True)})

    context = {
        'categorias': cursos,
        'form': form
    }
    return render(request, 'cursos/cursos.html', context)

# def candidatar(request):
#     if request.method=='POST':
#         print(request.POST)
#     to_json = {
#         "key1": "value1",
#         "key2": "value2"
#     }
#     return HttpResponse(json.dumps(to_json), mimetype='application/json')


@login_required
def candidatar(request, id):

    curso = Curso.objects.get(id=id)
    form = CadastroCandidatoForm(initial={'curso': curso})
    if request.method == 'POST':
        form = CadastroCandidatoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'cursos/cadastrar_candidato.html', context)


@login_required
def cadastrar_curso(request):
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
        else:
            print(form.errors)
    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)


@login_required
def editar_curso(request, id):
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
        else:
            print(form.errors)
    context = {
        'form': form,
        'CADASTRAR': 'EDITAR',
        'curso': curso
    }
    return render(request, 'cursos/adm_cursos_cad_edit.html', context)


@login_required
def listar_candidatos_curso(request, id):
    curso = Curso.objects.get(id=id)
    candidatos = Candidato.objects.filter(curso=curso)
    context = {
        'candidatos': candidatos,
        'CADASTRAR': 'EDITAR',
        'curso': curso
    }
    return render(request, 'cursos/listar_candidatos_curso.html', context)


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


def prematricula(request):
    form = CadastroCandidatoForm()
    categorias = Categoria.objects.all()
    cursos = []
    for i in categorias:
        cursos.append(
            {'categoria': i, 'curso': Curso.objects.filter(categoria=i, ativo=True)})

    form = CadastroCandidatoForm()
    if request.method == 'POST':
        form = CadastroCandidatoForm(request.POST)
        dtnascimento_cp = request.POST['dt_nascimento']
        dtnascimento_hr = datetime.strptime(dtnascimento_cp, '%Y-%m-%d')
        dt_nascimento = dtnascimento_hr.date()
        today = date.today()
        age = today.year - dt_nascimento.year - \
            ((today.month, today.day) < (dt_nascimento.month, dt_nascimento.day))
        teste = True
        candidato = ""

        try:
            cpf =  request.POST['cpf']
            candidato = Candidato.objects.get(cpf=cpf)
        except Exception as e:
            print(e)
            pass


        for i in request.POST.getlist('turmas'):

            turma = Turma.objects.get(id=i)
            if candidato:
                print(candidato.turmas.all())
                for t in candidato.turmas.all():
                    if t == turma:
                        messages.error(request, 'Candidato já cadastro no curso ' + turma.curso.nome)
                        return redirect('/prematricula')

                for t in candidato.turmas_selecionado.all():
                    if t == turma:
                        messages.error(request, 'Candidato já cadastro no curso ' + turma.curso.nome)
                        return redirect('/prematricula')

            if (turma.idade_min is not None and age < turma.idade_min) or (turma.idade_max is not None and age > turma.idade_max):
                teste = False
        if form.is_valid() and teste:
            print('valido')
            candidato = form.save()
            for i in request.POST.getlist('turmas'):
                candidato.turmas.add(i)
            messages.success(
                request, 'Pré-inscrição realizada com sucesso! Aguarde nosso contato para finalizar inscrição.')
            return redirect('/')
        else:
            print('n valido')
            if not teste:
                messages.error(
                    request, 'Não foi possível realizar a inscrição na turma: A idade não atende a faixa etária da turma.')
                return redirect('/prematricula')

            print(form.errors)
    context = {
        'form': form,
        'categorias': cursos
    }
    return render(request, 'cursos/pre_matricula.html', context)


def alterarCad(request):
    return render(request, 'cursos/alterar_cad.html')


@login_required
def administrativo(request):
    return render(request, 'cursos/administrativo.html')


@login_required
def turmas(request):
    return render(request, 'cursos/adm_turmas.html')


@login_required
def criar_turmas(request):
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
    return render(request, 'cursos/adm_turmas_criar.html', context)


@login_required
def listar_turmas(request):
    if request.user.is_superuser:
        turmas = Turma.objects.all()
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        turmas = Turma.objects.filter(curso__categoria=id_categoria)
    context = {
        'turmas': turmas
    }
    return render(request, 'cursos/adm_turmas_listar.html', context)


@login_required
def get_candidatos(request, id_curso):
    if request.user.is_staff:
        candidatos = Candidato.objects.filter(curso=id_curso)
    else:
        candidatos = {}
    context = {
        'candidatos': candidatos
    }
    return render(request, 'cursos/GET/get_candidatos.html', context)


@login_required
def adm_cursos(request):
    return render(request, 'cursos/adm_cursos.html')


@login_required
def listar_cursos(request):
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
    return render(request, 'cursos/adm_locais.html')


@login_required
def adm_locais_criar(request):
    form = CadastroLocalForm()
    if request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo local cadastrado!')
            return redirect('adm_locais_listar')
        else:
            print(form.errors)
    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'cursos/adm_locais_criar.html', context)


@login_required
def listar_locais(request):
    locais = Local.objects.all()
    context = {
        'locais': locais
    }
    return render(request, 'cursos/adm_locais_listar.html', context)


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
        else:
            print(form.errors)
    context = {
        'form': form,
        'local': local
    }
    return render(request, 'cursos/adm_locais_editar.html', context)


@login_required
def adm_locais_excluir(request, id):
    local = Local.objects.get(id=id)
    local.delete()
    return redirect('adm_locais_listar')


@login_required
def adm_categorias(request):
    return render(request, 'cursos/adm_categorias.html')


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
        else:
            print(form.errors)
    context = {
        'form': form,
        'CADASTRAR': 'NOVO'
    }
    return render(request, 'cursos/adm_categorias_criar.html', context)


@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'cursos/adm_categorias_listar.html', context)


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
        else:
            print(form.errors)
    context = {
        'form': form,
        'categoria': categoria
    }
    return render(request, 'cursos/adm_categorias_editar.html', context)


@login_required
def adm_professores(request):
    context = {}
    return render(request, 'cursos/adm_professores.html', context)


@login_required
def adm_professores_criar(request):
    form = CadastroProfessorForm()
    if request.method == 'POST':
        form = CadastroProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Instrutor cadastrada com sucesso!')
            return redirect('adm_professores')
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'cursos/adm_professores_criar.html', context)


@login_required
def adm_professores_listar(request):
    instrutores = Instrutor.objects.all()
    context = {
        'Instrutores': instrutores
    }
    return render(request, 'cursos/adm_professores_listar.html', context)


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
        else:
            print(form.errors)
    context = {
        'form': form,
        'instrutor': instrutor
    }
    return render(request, 'cursos/adm_professores_editar.html', context)


@login_required
def adm_professores_excluir(request, id):
    instrutor = Instrutor.objects.get(id=id)
    instrutor.delete()
    return redirect('adm_professores')


@login_required
def visualizar_turma(request, id):
    turma = Turma.objects.get(id=id)
    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    matriculas = Matricula.objects.filter(turma=turma)
    selecionados = Candidato.objects.filter(
        turmas__in=[turma], turmas_selecionado__in=[turma])
    candidatos = Candidato.objects.filter(
        turmas__in=[turma]).exclude(turmas_selecionado__in=[turma])
    if request.method == 'POST':
        for i in request.POST:
            if i != 'csrfmiddlewaretoken':
                candidato = Candidato.objects.get(id=i)
                candidato.turmas_selecionado.add(turma)
                candidato.save()
    context = {
        'turma': turma,
        'matriculas': matriculas,
        'selecionados': selecionados,
        'candidatos': candidatos,
        'qnt_alunos': len(matriculas)
    }
    return render(request, 'cursos/adm_turmas_editar.html', context)


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
    return render(request, 'cursos/adm_turmas_editar_turma.html', context)


@login_required
def visualizar_turma_selecionado(request, id, id_selecionado):
    turma = Turma.objects.get(id=id)

    def enviar_email(aluno):
        pass
        # message = f'Você foi inscrito no {turma.curso.nome}.'
        # if(turma.grupo_whatsapp):
        #     message += f'A turma possui um grupo do Whatsapp, que pode ser acessado pelo link: {turma.grupo_whatsapp}'
        # send_mail(f'Inscrição no curso {turma.curso.nome}', message, settings.EMAIL_HOST_USER, [aluno.email],fail_silently=False)

    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    matriculas = Matricula.objects.filter(turma=turma)
    if turma.qnt <= len(matriculas):
        messages.error(
            request, 'Turma cheia! Não é possível adicionar mais alunos.')
        return redirect('adm_turma_visualizar', id)

    selecionado = Candidato.objects.get(id=id_selecionado)
    birthDate = selecionado.dt_nascimento
    today = date.today()
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))

    form_responsavel = ''
    try:
        aluno = Aluno.objects.get(cpf=selecionado.cpf)
        form = CadastroAlunoForm(instance=aluno)
        if age < 18:
            try:
                responsavel = Responsavel.objects.get(aluno=aluno)
                form_responsavel = CadastroResponsavelForm(
                    instance=responsavel)
            except:
                responsavel = 'NE'
                form_responsavel = CadastroResponsavelForm()
        else:
            responsavel = 'NP'

    except:
        aluno = False
        if age < 18:
            form_responsavel = CadastroResponsavelForm()
        else:
            responsavel = 'NP'

        form = CadastroAlunoForm(
            initial={
                'nome': selecionado.nome,
                'celular': selecionado.celular,
                'email': selecionado.email,
                'dt_nascimento': selecionado.dt_nascimento,
                'sexo': selecionado.sexo,
                'endereco': selecionado.endereco,
                'bairro': selecionado.bairro,
                'cpf': selecionado.cpf
            }
        )
    if request.method == 'POST':
        # Candidato não é aluno e pode ser maior ou menor de idade/ Ele pode ou não precisar de um responsável
        if not aluno:
            form = CadastroAlunoForm(request.POST)
            if form.is_valid():

                # -----  O candidato é menor de idade
                if age < 18:
                    form_responsavel = CadastroResponsavelForm(request.POST)

                    if not form_responsavel.is_valid():
                        context = {
                            'form': form,
                            'form_responsavel': form_responsavel,
                            'turma': turma,
                            'selecionado': selecionado,
                        }
                        return render(request, 'cursos/adm_turmas_editar_selecionado.html', context)

                    responsavel = form_responsavel.save()
                    aluno = form.save()
                    responsavel.r_aluno = aluno
                    responsavel.save()

                # O candidato é maior de idade:
                aluno = form.save()
                matricula = Matricula(turma=turma, aluno=aluno)
                matricula.save()
                selecionado.turmas_selecionado.remove(turma)
                selecionado.turmas.remove(turma)
                selecionado.save()
                messages.success(
                    request, 'Novo aluno cadastrado no sistema e matriculado na disciplina com sucesso!')
                enviar_email(aluno)
                return redirect('adm_turma_visualizar', id)

        # Candidato é menor de idade e já aluno, mas não possui um responsável cadastrado
        if responsavel == 'NE':
            form = CadastroAlunoForm(request.POST, instance=aluno)
            form_responsavel = CadastroResponsavelForm()
            if form.is_valid():
                if not form_responsavel.is_valid():
                    form_responsavel = CadastroResponsavelForm(request.POST)

                    if not form_responsavel.is_valid():
                        context = {
                            'form': form,
                            'form_responsavel': form_responsavel,
                            'turma': turma,
                            'selecionado': selecionado,
                        }
                        return render(request, 'cursos/adm_turmas_editar_selecionado.html', context)

                    responsavel = form_responsavel.save()
                    aluno.save()
                    responsavel.r_aluno = aluno
                    responsavel.save()

                aluno = form.save()
                matricula = Matricula(turma=turma, aluno=aluno)
                matricula.save()
                selecionado.turmas_selecionado.remove(turma)
                selecionado.turmas.remove(turma)
                selecionado.save()
                messages.success(
                    request, 'Aluno matriculado na disciplina com sucesso!')
                enviar_email(aluno)
                return redirect('adm_turma_visualizar', id)

        # O candidato é maior de idade e é aluno
        if responsavel == 'NP':
            form = CadastroAlunoForm(request.POST, instance=aluno)
            if form.is_valid():
                aluno = form.save()
                matricula = Matricula(turma=turma, aluno=aluno)
                matricula.save()
                selecionado.turmas_selecionado.remove(turma)
                selecionado.turmas.remove(turma)
                selecionado.save()
                messages.success(
                    request, 'Aluno atualizado e matriculado na disciplina com sucesso!')
                enviar_email(aluno)
                return redirect('adm_turma_visualizar', id)

        # O candidato é menor de idade e já é aluno, mas não posssui responsável cadastrado
        form = CadastroAlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            if not form_responsavel.is_valid():
                form_responsavel = CadastroResponsavelForm(request.POST)

                if not form_responsavel.is_valid():
                    context = {
                        'form': form,
                        'form_responsavel': form_responsavel,
                        'turma': turma,
                        'selecionado': selecionado,
                    }
                    return render(request, 'cursos/adm_turmas_editar_selecionado.html', context)

                responsavel = form_responsavel.save()
                aluno.save()
                responsavel.r_aluno = aluno
                responsavel.save()

            matricula = Matricula(turma=turma, aluno=aluno)
            matricula.save()
            selecionado.turmas_selecionado.remove(turma)
            selecionado.turmas.remove(turma)
            selecionado.save()
            messages.success(
                request, 'O aluno foi matriculado na disciplina com sucesso!')
            enviar_email(aluno)
            return redirect('adm_turma_visualizar', id)

    context = {
        'form': form,
        'form_responsavel': form_responsavel,
        'turma': turma,
        'selecionado': selecionado,
    }
    return render(request, 'cursos/adm_turmas_editar_selecionado.html', context)


@login_required
def excluir_turma(request, id):
    turma = Turma.objects.get(id=id)

    if not request.user.is_superuser:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        if turma.curso.categoria != id_categoria:
            messages.error(
                request, 'Você não tem autorização para acessar essa turma.')
            return redirect('adm_turmas_listar')

    # matriculas=Matricula.objects.filter(turma=turma)
    # selecionados=Candidato.objects.filter(turmas__in=[turma], turmas_selecionado__in=[turma])
    # candidatos=Candidato.objects.filter(turmas__in=[turma]).exclude(turmas_selecionado__in=[turma])
    if request.user.is_superuser:
        turma.delete()

    context = {
        'turma': turma,
        # 'matriculas': matriculas,
        # 'selecionados': selecionados,
        # 'candidatos': candidatos,
        # 'qnt_alunos': len(matriculas)
    }
    return redirect('adm_turmas_listar')


def resultado(request):
    return render(request, 'cursos/resultado.html')


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if "next" in request.GET:
                return redirect(request.GET.get('next'))
            return redirect('/')
        else:
            context = {
                'error': True,
            }

    return render(request, 'registration/login.html', context)


@login_required
def adm_alunos_listar(request):
    if request.user.is_superuser:
        alunos = Aluno.objects.all()
    else:
        id_categoria = Categoria.objects.get(nome=request.user.groups.all()[0])
        alunos = Turma.objects.filter(curso__categoria=id_categoria)

    print(alunos)
    context = {
        'alunos': alunos
    }
    return render(request, 'cursos/adm_alunos_listar.html', context)


@login_required
def adm_alunos_visualizar(request, id):
    aluno = Aluno.objects.get(id=id)

    if not request.user.is_superuser:
        messages.error(
            request, 'Você não tem autorização para acessar essa turma.')
        return redirect('adm_alunos')

    aluno = Aluno.objects.get(id=id)
    try:
        responsavel = Responsavel.objects.get(r_aluno=aluno)
        menor = True
    except:
        responsavel = ''
        menor = False
    try:
        matriculas = Matricula.objects.filter(aluno=aluno)
    except:
        pass
    context = {
        'aluno': aluno,
        'responsavel': responsavel,
        'menor': menor,
        'matriculas': matriculas

    }

    return render(request, 'cursos/adm_aluno_visualizar.html', context)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def autenticar_data_candidato(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode("utf-8"))
        if not data['dt_nascimento']:
            return Exception("DEU MERDA, CADE a idade????")

        age = calculate_age(datetime.strptime(
            data['dt_nascimento'], '%Y-%m-%d'))
        return JsonResponse({'data': list(Turma.objects.filter((Q(idade_min__lte=age) | Q(idade_min__isnull=True)), (Q(idade_max__gte=age) | Q(idade_max__isnull=True))).values('id'))})
    else:
        raise PermissionDenied()
