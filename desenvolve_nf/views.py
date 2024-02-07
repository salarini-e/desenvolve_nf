#Importações das estruturas padrões do Django.
from django.shortcuts import render, redirect
from .forms import Solicitacao_de_cadastro_de_cameraForm
#Importações das estruturas das aplicações do projeto.
from .models import Carousel_Index, ClimaTempo, Solicitacao_newsletter
from .functions import ClimaTempoTemperaturas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa

def index(request):
    context = {
        'carousel': Carousel_Index.objects.filter(ativa=True),
        'titulo': 'Desenvolve NF - Página Inicial'
    }
    return render(request, 'desenvolve_nf/index.html', context)

def getClimaTempo(request):
    #processos
    ClimaTempoTemperaturas()
    
    #fim de processos
    context={

    }
    return render(request, 'cidade_inteligente.html', context)

def cidade_inteligente_home(request):
    clima = ClimaTempo.objects.first()
    context = {
        'titulo': 'Cidade Inteligente - Página Inicial',
        'clima': clima
    }
    return render(request, 'cidade_inteligente.html', context)

@login_required
def cidade_inteligente_cadastro_camera(request):
    clima = ClimaTempo.objects.first()
    if request.method == 'POST':
        form = Solicitacao_de_cadastro_de_cameraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitação de cadastro de câmera enviada com sucesso!')
            return redirect('cidade_inteligente_cadastro_camera')
    else:
        pessoa = Pessoa.objects.get(user=request.user)
        form = Solicitacao_de_cadastro_de_cameraForm(initial={'pessoa': pessoa})
    context = {
        'titulo': 'Cidade Inteligente - Cadastrar Câmera',
        'clima': clima,
        'form': form
    }
    return render(request, 'cadastro_camera.html', context)

def solicitarNewsLetter(request):
    if request.user.is_authenticated:
        try:
            pessoa = Pessoa.objects.get(user=request.user)
            Solicitacao_newsletter.objects.create(pessoa=pessoa)
            messages.success(request, 'Solicitação de cadastro enviada com sucesso!')
        except:
            print('Erro ao solicitar cadastro de Newsletter.')
            print(str(e))
            messages.error(request, 'Erro ao solicitar cadastro! Contate o administrador do sistema.')
        return redirect('index')
    else:
        messages.error(request, 'Você precisa estar logado para solicitar cadastro!')
        return redirect('autenticacao:login')
    
def error_500(request):
    return render(request, '500.html', status=500)

def carnaval(request):
    context = {
        'titulo': ' Carnaval 2024 - Programação'
    }
    return render(request, 'desenvolve_nf/carnaval.html', context)