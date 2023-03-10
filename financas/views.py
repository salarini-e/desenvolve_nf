from django.shortcuts import render
from django.apps import apps

# Create your views here.
def index(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'financas/index.html', context)

def alvara(request):
    return render('financas/list.html')