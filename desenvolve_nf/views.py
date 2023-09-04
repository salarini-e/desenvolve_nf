#Importações das estruturas padrões do Django.
from django.shortcuts import render
#Importações das estruturas das aplicações do projeto.
from .models import Carousel_Index, ClimaTempo
from .functions import ClimaTempoTemperaturas

def index(request):
    context = {
        'carousel': Carousel_Index.objects.filter(ativa=True)
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
    print(clima.turno())
    context = {
        'titulo': 'Cidade Inteligente',
        'clima': clima
    }
    return render(request, 'cidade_inteligente.html', context)