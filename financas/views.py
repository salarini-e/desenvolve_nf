from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'financas/index.html', context)

def alvara(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'financas/alvara.html', context)

def get_alvara(request, nome):
    arquivos={
        'requerimento_alvara': 'REQUERIMENTO-DE-ALVARA.pdf',
        'requerimento_baixa': 'REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'
    }
    context={
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': arquivos[nome]
    }
    return render(request, 'financas/get_alvara.html', context)