from django.shortcuts import render
from django.apps import apps


def index(request):
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
    }
    return render(request, 'financas/index.html', context)


def formularios(request, arg):
    arquivos = {
        'alvara': [['Requerimento Alvará', 'alvara/REQUERIMENTO-DE-ALVARA.pdf'],
                   ['REQUERIMENTO DE BAIXA DE DÉBITO',
                    'alvara/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                   ['requerimento_iss', 'alvara/REQUERIMENTO-DE-CERTIDAO-DE-ISS-E-ALVARA-1-4-1.pdf']],
        'itbi': [['IRequerimento Alvará', 'alvara/REQUERIMENTO-DE-ALVARA.pdf'],
                 ['IREQUERIMENTO DE BAIXA DE DÉBITO',
                  'alvara/REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf'],
                 ['Irequerimento_iss', 'alvara/REQUERIMENTO-DE-CERTIDAO-DE-ISS-E-ALVARA-1-4-1.pdf']]
    }

    # 'requerimento_revisao': 'REQUERIMENTO-DE-REVISAO-DE-TAXA-DE-ALVARA-1.pdf',
    # # Certidão
    # 'autorizacao_predial': 'AUTORIZACAO-VISTORIA-PREDIAL-3.pdf',
    # 'requerimento_escritura': 'REQUERIMENTO-DE-AVERBACAO-DE-ESCRITURA.pdf',
    # 'requerimento_certicao': 'REQUERIMENTO-DE-CERTIDAO-1.pdf',
    # # IPTU
    # 'requerimento_baixaDeb': 'REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf',
    # 'requerimento_inclusao': 'REQUERIMENTO-DE-INCLUSAO-DE-POSSUIDOR.pdf',
    # 'requerimento_recolhimento': 'REQUERIMENTO-DE-RECOLHIMENTO-DE-TRIBUTOS-1.pdf',
    # 'requerimento_reviptu': 'REQUERIMENTO-REVISAO-DE-IPTU-1.pdf',
    # # ITBI
    # 'declaracao_ciencia_itbi': 'DECLARACAO-DE-CIENCIA-DE-ITBI.pdf',
    # 'declaracao_transacao_imobiliaria': 'Declaracao-de-Transacao-Imo-biliaria-ITBI-PMNF-5.pdf',
    # 'requerimento_revisao_itbi': 'REQUERIMENTO-DE-REVISAO-DE-ITBI.pdf',
    # # Isenção
    # 'requerimento_imunidade_tributaria': 'REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf',
    # 'requerimento_isencao': 'REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf',
    # 'requerimento_insencao_nao_incidencia_tributaria': 'REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf',
    # 'requerimento_isencao_parcial_tombamento': 'REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf',
    # # Diversos
    # 'requerimento_imunidade_tributaria': 'REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf',
    # 'requerimento_isencao': 'REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf',
    # 'requerimento_insencao_nao_incidencia_tributaria': 'REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf',
    # 'requerimento_isencao_parcial_tombamento': 'REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf'

    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'arquivos': arquivos,
    }
    return render(request, 'financas/formularios.html', context)


def alvara(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/alvara.html', context)
    arquivos = {
        'requerimento_alvara': 'REQUERIMENTO-DE-ALVARA.pdf',
        'requerimento_baixa': 'REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf',
        'requerimento_iss': 'REQUERIMENTO-DE-CERTIDAO-DE-ISS-E-ALVARA-1-4-1.pdf',
        'requerimento_revisao': 'REQUERIMENTO-DE-REVISAO-DE-TAXA-DE-ALVARA-1.pdf'
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/alvara.html', context)


def certidao(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/certidao.html', context)
    tipos_arquivos = {
        'autorizacao_predial': 'AUTORIZACAO-VISTORIA-PREDIAL-3.pdf',
        'requerimento_escritura': 'REQUERIMENTO-DE-AVERBACAO-DE-ESCRITURA.pdf',
        'requerimento_certicao': 'REQUERIMENTO-DE-CERTIDAO-1.pdf'
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': tipos_arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/certidao.html', context)


def iptu(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/iptu.html', context)
    arquivos = {
        'requerimento_baixaDeb': 'REQUERIMENTO-DE-BAIXA-DE-DEBITO.pdf',
        'requerimento_inclusao': 'REQUERIMENTO-DE-INCLUSAO-DE-POSSUIDOR.pdf',
        'requerimento_recolhimento': 'REQUERIMENTO-DE-RECOLHIMENTO-DE-TRIBUTOS-1.pdf',
        'requerimento_reviptu': 'REQUERIMENTO-REVISAO-DE-IPTU-1.pdf'
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/iptu.html', context)


def itbi(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/itbi.html', context)
    tipos_arquivos = {
        'declaracao_ciencia_itbi': 'DECLARACAO-DE-CIENCIA-DE-ITBI.pdf',
        'declaracao_transacao_imobiliaria': 'Declaracao-de-Transacao-Imo-biliaria-ITBI-PMNF-5.pdf',
        'requerimento_revisao_itbi': 'REQUERIMENTO-DE-REVISAO-DE-ITBI.pdf'
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': tipos_arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/itbi.html', context)


def isencao(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/isencao.html', context)
    tipos_arquivos = {
        'requerimento_imunidade_tributaria': 'REQUERIMENTO-DE-IMUNIDADE-TRIBUTARIA-form.pdf',
        'requerimento_isencao': 'REQUERIMENTO-DE-ISENCAO-MEI-TFA-1.pdf',
        'requerimento_insencao_nao_incidencia_tributaria': 'REQUERIMENTO-DE-ISENCAO-NAO-INCIDENCIA-TRIBUTARIA.pdf',
        'requerimento_isencao_parcial_tombamento': 'REQUERIMENTO-DE-ISENCAO-PARCIAL-TOMBAMENTO.pdf'
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': tipos_arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/isencao.html', context)


def diversos(request, arg):
    if arg == 'opcoes':
        context = {
            'titulo': apps.get_app_config('financas').verbose_name,
            'arg': arg
        }
        return render(request, 'financas/diversos.html', context)
    arquivos = {
        'declaracao_residencia': 'DECLARACAO-DE-RESIDENCIA.pdf',
        'requerimento_adesao': 'REQUERIMENTO-DE-ADESAO.pdf',
        'requerimento_att_cadastral': 'REQUERIMENTO-DE-ATUALIZACAO-CADASTRAL-1.pdf',
        'requerimento_autonomo': 'REQUERIMENTO-PARA-AUTONOMO.pdf',
    }
    context = {
        'titulo': apps.get_app_config('financas').verbose_name,
        'url_pdf': arquivos[arg],
        'arg': arg
    }
    return render(request, 'financas/diversos.html', context)
