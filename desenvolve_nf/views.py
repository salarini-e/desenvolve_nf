from django.shortcuts import render
from .models import Carousel_Index

# Create your views here.
def index(request):
    context = {
        'carousel': Carousel_Index.objects.filter(ativa=True)
    }
    return render(request, 'index_desenvolvenf.html', context)


def cidade_inteligente_home(request):
    context = {
        'titulo': 'Cidade Inteligente'
    }
    return render(request, 'cidade_inteligente.html', context)