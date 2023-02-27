from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_desenvolvenf.html')


def cidade_inteligente_home(request):
    context = {
        'titulo': 'Cidade Inteligente'
    }
    return render(request, 'cidade_inteligente.html', context)