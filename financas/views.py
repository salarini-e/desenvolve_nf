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
                'certidao': [['Requerimento de Averbação de Escritura',
                              'certidoes/REQUERIMENTO-DE-AVERBACAO-DE-ESCRITURA.pdf'],
                             ['Requerimento de Certidão', 'certidoes/REQUERIMENTO-DE-CERTIDAO-1.pdf']],
                'iptu': [['Autorizacao para Vistoria Predial', 'certidoes/AUTORIZACAO-VISTORIA-PREDIAL-3.pdf'],
                         ['Requerimento de Baixa de Débito', 'iptu/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                         ['Requerimento de Inclusao de Possuidor', 'iptu/REQUERIMENTO-DE-INCLUSAO-DE-POSSUIDOR.pdf'],
                         ['requerimento_recolhimento', 'iptu/REQUERIMENTO-DE-RECOLHIMENTO-DE-TRIBUTOS-1.pdf'],
                         ['requerimento_revisao', 'iptu/REQUERIMENTO-REVISAO-DE-IPTU-1.pdf']],
                'itbi': [['Declaração Ciencia ITBI', 'itbi/DECLARACAO-DE-CIENCIA-DE-ITBI.pdf'],
                         ['Declaração Transacao Imobiliaria', 'itbi/Declaracao-de-Transacao-Imo-biliaria-ITBI-PMNF-5.pdf'],
                         ['Requerimento Revisao ITBI', 'itbi/REQUERIMENTO-DE-REVISAO-DE-ITBI.pdf']],
                'isencao': [['Requerimento Imunidade Tributaria', 'isencao/REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf'],
                            ['Requerimento Isenção',
                             'isencao/REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf'],
                            ['Requerimento Insencao Não Incidência Tributaria', 'isencao/REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf'], ['Requerimento Isenção Parcial Tombamento', 'isencao/REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf']],
                'diversos': [['Declaração de Residência', 'diversos/DECLARACAO-DE-RESIDENCIA.pdf'],
        ['Requerimento de Adesão',
         'diversos/REQUERIMENTO-DE-ADESAO.pdf'],
        ['Requerimento de Atualização Cadastral',
         'diversos/REQUERIMENTO-DE-ATUALIZACAO-CADASTRAL-1.pdf'],
       
    ]}
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'arquivos': arquivos,
    }
    return render(request, 'financas/formularios.html', context)
