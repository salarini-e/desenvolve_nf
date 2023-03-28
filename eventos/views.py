from django.shortcuts import render
from django.apps import apps
# Create your views here.

def index(request):
    context={
        'titulo': apps.get_app_config('eventos').verbose_name,
    }
    return render(request, "index.html", context)