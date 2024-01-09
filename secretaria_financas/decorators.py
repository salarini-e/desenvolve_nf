from .models import Funcionarios
from django.shortcuts import redirect
from django.contrib import messages

def funcionario_financas_required(view_func):
    def _wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                print('super user')
                return view_func(request, *args, **kwargs)
            
            try:
                funcionario_financas = Funcionarios.objects.get(user=request.user)
            except Exception as e:
                funcionario_financas = None

            if funcionario_financas:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'Você não tem permissão para acessar esta página.')
                return redirect('empreendedor:index')
        else:
            return redirect('login')
    return _wrapper

def setor_financas_required(view_func):
    def _wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                print('super user')
                return view_func(request, *args, **kwargs)
            
            try:
                funcionario_financas = Funcionarios.objects.get(user=request.user)
            except Exception as e:
                funcionario_financas = None

            if funcionario_financas:
                for setor in setor_:
                    if funcionario_financas.setor.nome.lower() == setor.lower():
                        return view_func(request, *args, **kwargs)
                messages.error(request, 'Você não tem permissão para acessar esta página.')
                return redirect('empreendedor:index')
                    
            else:
                messages.error(request, 'Você não tem permissão para acessar esta página.')
                return redirect('empreendedor:index')
        else:
            return redirect('login')
    return _wrapper