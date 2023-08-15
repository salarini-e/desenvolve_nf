from django.shortcuts import render
from ..forms import FormEmpresa
# Create your views here.
def minha_empresa(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/index.html', context)

def cadastrar_empresa(request):
    form=FormEmpresa()
    context = {
        'titulo': 'Sala do Empreendedor',
        'form': form
    }
    return render(request, 'sala_do_empreendedor/minha-empresa/cadastro_empresa.html', context)
