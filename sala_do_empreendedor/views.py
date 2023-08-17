from django.shortcuts import render
from .api import ApiProtocolo
from .views_folder.minha_empresa import *
from .views_folder.vitrine_virtual import *

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

#views do QUERO SER MEI
def por_que_ser_mei(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/por-que-ser-mei.html', context)
def o_que_precisa_saber_para_ser_mei(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/o-que-voce-precisa-saber-antes-de-se-tornar-um-mei.html', context)
def jornada_empreendedora(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/jornada-empreendedora.html', context)
def documentosNecessarios(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/documentosNecessarios.html', context)

def quaisAsOcupacoesQuePodemSerMei(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/quaisAsOcupacoesQuePodemSerMei.html', context)

def dicasDeSegurancaDaVigilanciaSanitaria(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/dicasDeSegurancaDaVigilanciaSanitaria.html', context)

def dicasDeSegurançaDoCorpoDeBombeiros(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/dicasDeSegurançaDoCorpoDeBombeiros.html', context)

def dicasDeMeioAmbiente(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/dicasDeMeioAmbiente.html', context)

def prepareSe(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/prepareSe.html', context)

def transportadorAutonomoDeCargas(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/transportadorAutonomoDeCargas.html', context)

def direitosEObrigacoes(request):
    context = {
        'titulo':'Sala do Empreendedor',
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/direitosEObrigacoes.html', context)

def registrocadastur(request):
    context = {
         'titulo': 'Sala do Empreendedor'
    }
    return render(request, 'sala_do_empreendedor/quero-ser-mei/registrocadastur.html', context)

def ja_sou_mei(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/ja-sou-mei.html', context)

def emissaoDeComprovante(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/emissaoDeComprovante.html', context)

def atualizacaoCadastral(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/atualizacaoCadastral.html', context)

def capacita(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/capacita.html', context)

def notaFiscal(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/notaFiscal.html', context)

def relatorioMensal(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/relatorioMensal.html', context)

def pagamentoDeContribuicaoMensal(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/pagamentoDeContribuicaoMensal.html', context)

def solucoesFinanceiras(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/solucoesFinanceiras.html', context)

def certidoesEComprovantes(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/certidoesEComprovantes.html', context)

def declaracaoAnualDeFaturamento(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/declaracaoAnualDeFaturamento.html', context)

def dispensaDeAlvara(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/jaSouMei/dispensaDeAlvara.html', context)

def abertura_de_empresa(request):
    context = {
         'titulo': 'Sala do Empreendedor',
        # 'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'sala_do_empreendedor/abertura-de-empresa.html', context)

