from sala_do_empreendedor.models import Andamento_Processo_Digital

from django.core.mail import send_mail
from django.conf import settings

from .models import (StatusDocumentosRequerimentoISS, StatusDocumentosLicencaSanitaria, StatusDocumentosLicencaAmbiental,
                     DocumentosLicencaAmbiental, DocumentosLicencaSanitaria, DocumentosRequerimentoISS, DOC_STATUS_CHOICES)
from .forms.requerimento_iss import (Documentos_ISS_Form, DocumentosLicencaAmbiental_Form, DocumentosLicencaSanitaria_Form, 
                                     Documentos_ISS_SEM_DIPLOMA_Form)

def send_email_for_create_process(processo, andamento):
    pass

def generic_send_email(assunto, mensagem, destinatarios):
    try:
        send_mail(
            assunto,
            mensagem,
            settings.DEFAULT_FROM_EMAIL,
            destinatarios,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")
        return False

def upload_forms(requerimento_iss):
    '''
    Essa função é para ajustar os formulários de acordo com as condições do requerimento de ISS
    '''
    # Verifica a escolaridade da profissão associada ao requerimento
    # Se a escolaridade for entre 1 e 4, utiliza o formulário sem diploma
    # Caso contrário, utiliza o formulário com diploma
    if requerimento_iss.profissao.escolaridade.id in [1, 2, 3, 4]:
        form_1 = Documentos_ISS_SEM_DIPLOMA_Form(initial={'requerimento': requerimento_iss.id})
    else:
        form_1 = Documentos_ISS_Form(initial={'requerimento': requerimento_iss.id})

    # Inicializa os formulários para Licença Ambiental e Licença Sanitária
    form_2 = DocumentosLicencaAmbiental_Form(initial={'requerimento': requerimento_iss.id})
    form_3 = DocumentosLicencaSanitaria_Form(initial={'requerimento': requerimento_iss.id})

    # Ajusta os campos dos formulários baseados nas condições do requerimento

    # Se o requerimento é de um autônomo localizado
    if requerimento_iss.autonomo_localizado == 's':
        # Se a profissão não possui licença sanitária com alvará
        if not requerimento_iss.profissao.licenca_sanitaria_com_alvara:
            # Se a profissão não possui licença sanitária
            if not requerimento_iss.profissao.licenca_sanitaria:
                # Exclui campos específicos relacionados à licença sanitária do formulário 3
                for field in ['comprovante_ar_condicionado', 'comprovante_limpeza_caixa_dagua', 'plano_gerenciamento_de_residuos', 'licenca_sanitaria']:
                    if field in form_3.fields:
                        form_3.fields.pop(field)
    else:
        # Se não é um autônomo localizado, exclui o campo 'espelho_iptu' do formulário 1
        if 'espelho_iptu' in form_1.fields:
            form_1.fields.pop('espelho_iptu')
        # Se a profissão não possui licença sanitária, exclui campos relacionados à licença sanitária do formulário 3
        if not requerimento_iss.profissao.licenca_sanitaria:
            for field in ['comprovante_ar_condicionado', 'comprovante_limpeza_caixa_dagua', 'plano_gerenciamento_de_residuos', 'licenca_sanitaria']:
                if field in form_3.fields:
                    form_3.fields.pop(field)

    # Se a profissão não possui licença ambiental, exclui campos relacionados à licença ambiental do formulário 2
    if not requerimento_iss.profissao.licenca_ambiental:
        for field in ['licenca_ambiental', 'contrato_locacao', 'conta_dagua', 'foto', 'croqui_acesso']:
            if field in form_2.fields:
                form_2.fields.pop(field)
    
    # Retorna os três formulários ajustados
    return form_1, form_2, form_3

def get_status_documentos(requerimento_iss):
    # Verifica se existem status dos documentos do requerimento ISS
    # Se não existir, retorna None... Existem casos em que o requerimento não possui licença sanitária ou ambiental.
    # Assim, não sei se faz sentido o Try no ISS, mas tá aí. 
    status_documentos = {}
    try:
        status_documentos['iss'] = StatusDocumentosRequerimentoISS.objects.get(requerimento=requerimento_iss)
    except StatusDocumentosRequerimentoISS.DoesNotExist:
        status_documentos['iss'] = None
    try:
        status_documentos['sanitaria'] = StatusDocumentosLicencaSanitaria.objects.get(requerimento=requerimento_iss)
    except StatusDocumentosLicencaSanitaria.DoesNotExist:
        status_documentos['sanitaria'] = None

    try:
        status_documentos['ambiental'] = StatusDocumentosLicencaAmbiental.objects.get(requerimento=requerimento_iss)
    except StatusDocumentosLicencaAmbiental.DoesNotExist:
        status_documentos['ambiental'] = None

    return status_documentos

def get_context_for_acompanhamento(requerimento):
    #Montei o contexto aqui só para na views.py ficar mais limpa
    andamentos = Andamento_Processo_Digital.objects.filter(processo__n_protocolo=requerimento.processo.n_protocolo).order_by('-id')
    docs = StatusDocumentosRequerimentoISS.objects.filter(requerimento=requerimento).first()
    
    context = {
        'processo': requerimento.processo,
        'requerimento': requerimento,
        'documentos': {
            'iss': DocumentosRequerimentoISS.objects.filter(requerimento=requerimento).first(),
            'sanitaria': DocumentosLicencaSanitaria.objects.filter(requerimento=requerimento).first(),
            'ambiental': DocumentosLicencaAmbiental.objects.filter(requerimento=requerimento).first(),
        },
        'status': get_status_documentos(requerimento),
        'andamentos': andamentos,
        'is_concluded': requerimento.processo.status == 'cn',
        'is_approved': requerimento.processo.status == 'ar',
        'show_licenca_ambiental': requerimento.profissao.licenca_ambiental,
        'show_licenca_sanitaria': requerimento.profissao.licenca_sanitaria or requerimento.profissao.licenca_sanitaria_com_alvara,
        'show_autonomo_localizado': requerimento.autonomo_localizado == 's' and requerimento.profissao.licenca_sanitaria_com_alvara,
        'status_pagamento_ma': andamentos.first().verificar_boleto_ma() if andamentos.exists() else 'nada_para_exibir',
        'status_pagamento_ls': andamentos.first().verificar_boleto_ls() if andamentos.exists() else 'nada_para_exibir',        
        'status_choices': DOC_STATUS_CHOICES,
        'docs_aprovados': docs.validate_status(),
    }

    return context