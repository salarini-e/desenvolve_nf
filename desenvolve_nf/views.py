from django.shortcuts import render
from .models import Carousel_Index
from .models import ClimaTempo

# Create your views here.
def index(request):
    context = {
        'carousel': Carousel_Index.objects.filter(ativa=True)
    }
    return render(request, 'index_desenvolvenf.html', context)

def cidade_inteligente(request):
    #processos
    climaTempo = ClimaTempo.objects.all()[0]
    
    #fim de processos
    context={
        'climaTempo': climaTempo
    }
    return render(request, 'cidade_inteligente.html', context)

def cidade_inteligente_home(request):
    context = {
        'titulo': 'Cidade Inteligente'
    }
    return render(request, 'cidade_inteligente.html', context)