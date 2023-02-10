from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from cursos.forms import Aluno_form

from cursos.models import Aluno
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.


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
            return redirect('/')
        else:
            context = {
                'error': True,
            }
    return render(request, 'adm/login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')


def cadastro_user(request):
    
    form_pessoa = ''
    pessoa = ''
    is_user = False

    if request.user.is_authenticated:
        is_user = True

        try:
            pessoa = Pessoa.objects.get(user=request.user)
            form_pessoa = Form_Pessoa(initial={'email': request.user.email}, instance=pessoa)
            
        except Exception as e:
            form_pessoa = Form_Pessoa(initial={'email': request.user.email})
    else:
        form_pessoa = Form_Pessoa()

    if request.method == "POST":
        if pessoa:
            form_pessoa = Form_Pessoa(request.POST, instance=pessoa)
        else:
            form_pessoa = Form_Pessoa(request.POST)

        if form_pessoa.is_valid():

            # com o objetivo de diminuir a identação, e não sendo possível utilizar guard clauses, optei em 
            # verificar o is_user duas vezes
            if is_user or request.POST['password'] == request.POST['password2']:
                if is_user or len(request.POST['password']) >= 8:
                    try:
                        user = ''

                        if is_user:
                            user = User.objects.get(id=request.user.id)
                            user.email = request.POST['email']
                            user.save()
                        else:
                            user = User.objects.create_user(
                                username=request.POST['email'], email=request.POST['email'], password=request.POST['password'])
                            user.first_name = request.POST['nome']
                            user.save()

                        pessoa = form_pessoa.save(commit=False)
                        pessoa.user = user

                        pessoa.save()
                        messages.success(
                            request, 'Usuário cadastrado com sucesso!')
                        return redirect('/login')
                    except Exception as e:
                        messages.error(
                            request, 'Email de usuário já cadastrado')
                        
                messages.error(
                    request, 'A senha deve possuir pelo menos 8 caracteres')
            else:
                # as senhas não se coincidem
                messages.error(request, 'As senhas digitadas não se coincidem')
    context = {
        'form_pessoa': form_pessoa,
        'is_user': is_user
    }
    return render(request, 'adm/cadastro.html', context)

@login_required
def cadastro_aluno(request):
    form_aluno = Aluno_form()
    pessoa = Pessoa.objects.get(user=request.user)

    if request.method == 'POST':
        form = Aluno_form(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.pessoa = pessoa
            aluno.save()

            messages.success(request, "Cadastro completo!")
            return redirect('home')


    context = {
        'form': form_aluno
    }

    return render(request, 'adm/completar_cadastro.html', context)
