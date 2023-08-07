from django.shortcuts import render
from .api import ApiProtocolo

# Create your views here.
def index(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/index.html', context)

def em_construcao(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/em-construcao.html', context)

def consultar_protocolo(request):
    api = ApiProtocolo()
    status, response = api.recuperarAssuntos()
    print(response)
    message=response['message']
    if request.method == 'POST':
        
        status, message = api.recuperarProcesso(request.POST['cpf'])
        
    context = {
         'titulo': 'Sala do Empreendedor',
         'status': status,
         'message': message
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/consultar-protocolo.html', context)

def faccao_legal(request):
    context = {
        'titulo': 'Sala do Empreendedor',
        'titulo_pag':'Facção Legal',
    }
    return render(request, 'sala_do_empreendedor/em-construcao.html', context)

def vitrine_virtual(request):
    context = {
        'titulo': 'Sala do Empreendedor',
        'titulo_pag': 'Vitrine Virtual',
    }
    return render(request, 'sala_do_empreendedor/em-construcao.html', context)

def quero_ser_mei(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei.html', context)

def ja_sou_mei(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/ja-sou-mei.html', context)