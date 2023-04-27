from django.shortcuts import render
from django.apps import apps
from eventos.models import Evento


def index(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'eventos': Evento.objects.filter(app_name='financas')
    }
    return render(request, 'financas/index.html', context)


def formularios(request):
    arquivos = {'alvara': [['Requerimento Alvará', 'alvara/REQUERIMENTO-DE-ALVARA.pdf'],
                           ['Requerimento de Baixa de Débito',
                           'alvara/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                           ['Requerimento de Certidão de ISS e Alvará', 'alvara/ REQUERIMENTO-DE-CERTIDAO-DE-ISS-E-ALVARA-1-4-1.pdf'], ['Requerimento de Revisão de Taxa de Alvará', 'REQUERIMENTO-DE-REVISAO-DE-TAXA-DE-ALVARA-1.pdf']],
                'certidao': [['Autorizacao para Vistoria Predial', 'certidoes/AUTORIZACAO-VISTORIA-PREDIAL-3.pdf'],
                             ['Requerimento de Averbação de Escritura',
                              'certidoes/REQUERIMENTO-DE-AVERBACAO-DE-ESCRITURA.pdf'],
                             ['Requerimento de Certidão', 'certidoes/REQUERIMENTO-DE-CERTIDAO-1.pdf']],
                'iptu': [['Requerimento de Baixa de Débito', 'iptu/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                         ['Requerimento de Inclusao de Possuidor',
                          'iptu/REQUERIMENTO-DE-INCLUSAO-DE-POSSUIDOR.pdf'],
                         ['requerimento_recolhimento',
                          'iptu/REQUERIMENTO-DE-RECOLHIMENTO-DE-TRIBUTOS-1.pdf'],
                         ['requerimento_revisao', 'iptu/REQUERIMENTO-REVISAO-DE-IPTU-1.pdf']],
                'itbi': [['declaracao de ciencia para itbi', 'itbi/DECLARACAO-DE-CIENCIA-DE-ITBI.pdf'],
                         ['declaracao de transacao imobiliaria',
                          'itbi/Declaracao-de-Transacao-Imo-biliaria-ITBI-PMNF-5.pdf'],
                         ['requerimento de revisao de itbi', 'itbi/REQUERIMENTO-DE-REVISAO-DE-ITBI.pdf']],
                'isencao': [['requerimento de imunidade tributaria', 'isencao/REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf'],
                            ['requerimento de isencao',
                             'isencao/REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf'],
                            ['requerimento de insencao ou nao incidencia tributaria', 'isencao/REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf'], ['requerimento de isencao parcial do iptu por tombamento', 'isencao/REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf']],
                'diversos': [
        ['Declaração de Residência', 'diversos/DECLARACAO-DE-RESIDENCIA.pdf'],
        ['Requerimento de Adesão',
         'diversos/REQUERIMENTO-DE-ADESAO.pdf'],
        ['Requerimento de Atualização Cadastral',
         'diversos/REQUERIMENTO-DE-ATUALIZACAO-CADASTRAL-1.pdf'],
        ['Requerimento para Autonomo',
         'diversos/REQUERIMENTO-PARA-AUTONOMO.pdf']
    ]}
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'arquivos': arquivos,
    }
    return render(request, 'financas/formularios.html', context)
