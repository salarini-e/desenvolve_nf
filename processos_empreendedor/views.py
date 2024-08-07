from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from sala_do_empreendedor.forms import Criar_Processo_Form
from sala_do_empreendedor.models import Tipo_Processos, Andamento_Processo_Digital, Processo_Digital
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (RequerimentoISS, StatusDocumentosRequerimentoISS, StatusDocumentosLicencaSanitaria,
                      StatusDocumentosLicencaAmbiental, DocumentosRequerimentoISS, DocumentosLicencaSanitaria, 
                      DocumentosLicencaAmbiental, Relatorios, BoletosRequerimentoISS, AgentesRelatorios)
from .forms.requerimento_iss import (Processo_ISS_Form, Documentos_ISS_Form, DocumentosLicencaAmbiental_Form, DocumentosLicencaSanitaria_Form, Documentos_ISS_SEM_DIPLOMA_Form)
from .functions import send_email_for_create_process, upload_forms, get_context_for_acompanhamento, generic_send_email
from django.forms.models import model_to_dict
from guardiao.models import TentativaBurla
from django.db import transaction
from sala_do_empreendedor.models import Agente_Ambiental, Agente_Sanitario, Agente_Tributario, Agente
from django.db.models import Q
from autenticacao.models import Pessoa
from notification.models import Notification

@login_required
def novo_processo(request):
    return render(request, 'processos/novo_processo.html', {})


@login_required()
def listar_processos(request):
    agente = {
        'is_sanitario': Agente_Sanitario.objects.filter(user=request.user).exists(),
        'is_ambiental': Agente_Ambiental.objects.filter(user=request.user).exists(),
        'is_tributario': Agente_Tributario.objects.filter(user=request.user).exists(),
    }
    processos = Processo_Digital.objects.filter(solicitante=request.user).order_by('-dt_solicitacao')    
    paginator = Paginator(processos, 50)
    paginas = paginator.get_page(request.GET.get('page'))
    
    context = {
        'titulo': 'Processos digitais',
        'meus_processos': paginas,
        'agente': agente,
        'processos': 'ops',
        'is_agente': agente['is_sanitario'] or agente['is_ambiental'] or agente['is_tributario']
    }
    return render(request, 'processos/listar_processos.html', context)

@login_required()
def listar_processos_agente(request, tipo):

    agente_sanitario = Agente_Sanitario.objects.filter(user=request.user)
    agente_ambiental = Agente_Ambiental.objects.filter(user=request.user)
    agente_tributario = Agente_Tributario.objects.filter(user=request.user)

    if tipo == 'agente-sanitario' and agente_sanitario.exists():        
        documentos = StatusDocumentosLicencaSanitaria.objects.filter(
            Q(requerimento__profissao__licenca_sanitaria=True) |
            Q(requerimento__profissao__licenca_sanitaria_com_alvara=True)
        ).order_by('id')
        label = 'Agente sanitário'
    elif tipo == 'agente-ambiental' and agente_ambiental.exists():        
        documentos = StatusDocumentosLicencaAmbiental.objects.filter(requerimento__profissao__licenca_ambiental=True)
        label = 'Agente ambiental'
    elif tipo == 'agente-tributario' and agente_tributario.exists():
        documentos = StatusDocumentosRequerimentoISS.objects.all()
        label = 'Agente da sala do empreendedor'
    else:
        messages.error(request, 'Você não possui permissão para acessar essa página.')
        return redirect('processos_sempreendedor:listar_processos')
    
    context = {
        'titulo': 'Processos digitais',
        'documentos': documentos,
        'label': label,
        'tipo': tipo
    }
    
    return render(request, 'processos/listar_processos_agente.html', context)
   
@login_required()
def middle_acompanhamento_processo(request, n_protocolo):
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    
    if processo.tipo_processo.id == 1:
        return redirect('processos_empreendedor:acompanhamento_requerimento_iss', n_protocolo=n_protocolo)
    else:
        messages.error(request, 'Ocorreu um erro ao carregar seu processo. Informe juntamente o nº de protocolo {}'.format(n_protocolo))
    return redirect('processos_sempreendedor:listar_processos')

@login_required()
def middle_acompanhamento_processo_agente(request, tipo, n_protocolo):
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    
    if processo.tipo_processo.id == 1:
        return redirect('processos_empreendedor:acompanhamento_requerimento_iss_agente', tipo=tipo, n_protocolo=n_protocolo)
    else:
        messages.error(request, 'Ocorreu um erro ao carregar seu processo. Informe juntamente o nº de protocolo {}'.format(n_protocolo))
    return redirect('processos_sempreendedor:listar_processos')


@login_required
def acompanhamento_requerimento_iss(request, n_protocolo):
    requerimento_iss = get_object_or_404(RequerimentoISS, processo__n_protocolo=n_protocolo)

    documentos = {
        'iss': DocumentosRequerimentoISS.objects.filter(requerimento=requerimento_iss).exists(),
        'sanitaria': DocumentosLicencaSanitaria.objects.filter(requerimento=requerimento_iss).exists(),
        'ambiental': DocumentosLicencaAmbiental.objects.filter(requerimento=requerimento_iss).exists(),
    }
    
    if documentos['iss']:
        context = get_context_for_acompanhamento(requerimento_iss)
        return render(request, 'requerimentos_iss/contribuinte/acompanhamento.html', context)
    return redirect('processos_empreendedor:requerimento_iss_upload', n_protocolo=n_protocolo)

def notificar_situacao_documentos(request, tipo, n_protocolo):
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    requerimento_iss = RequerimentoISS.objects.get(processo=processo)
    if tipo == 'agente-tributario':
        documentos = StatusDocumentosRequerimentoISS.objects.get(requerimento=requerimento_iss)
    elif tipo == 'agente-ambiental':
        documentos = StatusDocumentosLicencaAmbiental.objects.get(requerimento=requerimento_iss)
    elif tipo == 'agente-sanitario':
        documentos = StatusDocumentosLicencaSanitaria.objects.get(requerimento=requerimento_iss)
    url_do_processo = f'http://localhost:8000/processos/acompanhamento/{n_protocolo}/requerimento-iss/'
    response = generic_send_email(
        assunto = 'Documentos do requerimento ISS', 
        mensagem = f'''Os status dos documentos do requerimento ISS do processo {n_protocolo} foram atualizados. Verifique a situação dos documentos:
        {url_do_processo}''', 
        destinatarios = [processo.solicitante.email]
        )
    return redirect('processos_empreendedor:acompanhamento_requerimento_iss_agente', tipo=tipo, n_protocolo=n_protocolo)
    
@login_required
def acompanhamento_requerimento_iss_agente(request, tipo, n_protocolo):
    requerimento_iss = get_object_or_404(RequerimentoISS, processo__n_protocolo=n_protocolo)

    documentos = {
        'iss': DocumentosRequerimentoISS.objects.filter(requerimento=requerimento_iss).exists(),
        'sanitaria': DocumentosLicencaSanitaria.objects.filter(requerimento=requerimento_iss).exists(),
        'ambiental': DocumentosLicencaAmbiental.objects.filter(requerimento=requerimento_iss).exists(),
    }
    
    if documentos['iss']:
        context = get_context_for_acompanhamento(requerimento_iss)
        context['tipo'] = tipo
        context['relatorios'] = Relatorios.objects.filter(processo=requerimento_iss.processo, aprovado=True).order_by('-id')
        if tipo == 'agente-tributario':
            label = 'Agente tributário'
        elif tipo == 'agente-ambiental':
            label = 'Agente ambiental'
        elif tipo == 'agente-sanitario':
            label = 'Agente sanitário'
        context['label'] = label
        return render(request, 'requerimentos_iss/agentes/acompanhamento.html', context)
    messages.warning(request, 'Aguardando envio de documentos.')
    return redirect('processos_empreendedor:listar_processos', n_protocolo=n_protocolo)
    

@login_required()
def requerimento_iss(request):
    
    if request.method == 'POST':
        form = Criar_Processo_Form(request.POST, request.FILES)
        form_iss = Processo_ISS_Form(request.POST)
        
        if form.is_valid() and form_iss.is_valid():
            processo = form.save(commit=False)
            processo.tipo_processo = Tipo_Processos.objects.get(id=1)
            processo.solicitante = request.user
            processo.status = 'ae'
            processo.save()
            processo_iss = form_iss.save(commit=False)
            processo_iss.processo = processo
            processo_iss.save()

            messages.success(request, 'Processo iniciado. Agora, envie os documentos necessários.')
            
            andamento = Andamento_Processo_Digital(
                processo=processo,              
                status='ae',
                observacao='Processo iniciado. Aguardando envio de documentos.',
                servidor=None
            )
            andamento.save()    
            Notification.objects.create(
                for_user = request.user,
                icone = '<i class="text-success fa-solid fa-list-check my-auto me-4"></i>',
                referencia = f'Protocolo #{processo.n_protocolo}',
                mensagem = 'Aguardando envio dos documentos.',
                url_redirect = reverse('processos_empreendedor:middle_acompanhamento_processo', args=[processo.n_protocolo])        
            )
            # Redireciona para a página de upload de documentos do requerimento ISS
            return redirect('processos_empreendedor:requerimento_iss_upload', n_protocolo=processo.n_protocolo) 
        else:
            print(form.errors)
    else:
        form = Criar_Processo_Form(initial={'tipo_processo': 1, 'solicitante': request.user.id})
        form_iss = Processo_ISS_Form(initial={'solicitante': request.user.id})
    
    context = {
        'titulo': 'Processos digitais',
        'form': form,
        'form_iss': form_iss,
    }
    return render(request, 'requerimentos_iss/1_form_iniciar_processo.html', context)

@login_required()
def requerimento_iss_upload_documentos(request, n_protocolo):
    
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    requerimento_iss = RequerimentoISS.objects.get(processo=processo)

    # Verificando se existe algum status dos documentos do requerimento ISS para ver se o arquivo já foi enviado
    try:        
        status = StatusDocumentosRequerimentoISS.objects.get(requerimento=requerimento_iss)
    except StatusDocumentosRequerimentoISS.DoesNotExist:    
        status = False

    # Se o status dos documentos já foi iniciado, exibe uma mensagem de aviso e redireciona
    if status:
        messages.warning(request, 'Processo já iniciado. Aguarde a avaliação dos documentos.')
        return redirect('empreendedor:andamento_processo', protocolo=n_protocolo)

    if request.method == 'GET':
        form_1, form_2, form_3 = upload_forms(requerimento_iss)
    elif request.method == 'POST':
        form_1 = Documentos_ISS_SEM_DIPLOMA_Form(request.POST, request.FILES)
        form_2 = DocumentosLicencaAmbiental_Form(request.POST, request.FILES)
        form_3 = DocumentosLicencaSanitaria_Form(request.POST, request.FILES)

        if form_1.is_valid() and form_2.is_valid() and form_3.is_valid():
            
            try:
                documentos_1 = form_1.save(commit=False)
                documentos_1.requerimento = requerimento_iss
                documentos_1.user_register = request.user
                documentos_1.save()
                documentos_1.create_status()

                documentos_2 = form_2.save(commit=False)
                documentos_2.requerimento = requerimento_iss
                documentos_2.user_register = request.user
                documentos_2.save()
                documentos_2.create_status()
                
                documentos_3 = form_3.save(commit=False)
                documentos_3.requerimento = requerimento_iss
                documentos_3.user_register = request.user
                documentos_3.save()
                documentos_3.create_status()

                andamento = Andamento_Processo_Digital(
                                processo=processo,              
                                status='nv',
                                observacao='Processo criado. Aguardando avaliação do pedido.',
                                servidor=None
                            )
                andamento.save()
                
                processo.status = 'nv'
                processo.save() 

                notification = Notification.objects.create(
                    for_user = requerimento_iss.processo.solicitante,
                    icone = '<i class="text-success fa-solid fa-list-check my-auto me-4"></i>',
                    referencia = f'Protocolo #{processo.n_protocolo}',
                    mensagem = 'Seu processo foi criado com sucesso!',
                    url_redirect = reverse('processos_empreendedor:middle_acompanhamento_processo', args=[processo.n_protocolo])

                )
            except IntegrityError:
                messages.error(request, 'Erro ao enviar os documentos. O nome dos arquivos anexados não devem conter acentos, cedilha ou caracteres especiais.')
                return redirect('processos_empreendedor:requerimento_iss_upload', protocolo=n_protocolo)
            
          
            if request.user.is_staff:
                return redirect('processos_empreendedor:listar_processos')
            else:
                return redirect('processos_empreendedor:listar_processos')        
    
    context = {
        'titulo': 'Processos digitais',
        'form_1': form_1,
        'form_2': form_2,
        'form_3': form_3,
        'processo': processo,  
        'requerimento': requerimento_iss,  
    }
    return render(request, 'requerimentos_iss/2_form_upload_arquivos.html', context)
  
@login_required
def atualizar_documento(request, n_protocolo, doc):
    requerimento_iss = get_object_or_404(RequerimentoISS, processo__n_protocolo=n_protocolo)

    documentos = {
        'iss': DocumentosRequerimentoISS.objects.filter(requerimento=requerimento_iss),
        'sanitaria': DocumentosLicencaSanitaria.objects.filter(requerimento=requerimento_iss),
        'ambiental': DocumentosLicencaAmbiental.objects.filter(requerimento=requerimento_iss),
    }

    if documentos['iss'].exists():     
        try:
            processo = Processo_Digital.objects.get(n_protocolo = n_protocolo)
            if processo.tipo_processo.id == 1:
                status = {}                
                status.update(model_to_dict(StatusDocumentosRequerimentoISS.objects.get(requerimento = requerimento_iss)))
                if documentos['sanitaria'].exists():
                    status.update(model_to_dict(StatusDocumentosLicencaSanitaria.objects.get(requerimento = requerimento_iss)))
                if documentos['ambiental'].exists():
                    status.update(model_to_dict(StatusDocumentosLicencaAmbiental.objects.get(requerimento = requerimento_iss)))
                print(status)
            try:
                status_doc = status[f"{doc}_status"]
            except Exception as e:
                messages.warning(request, 'Este documento não existe. Está tentando burlar o sistema? Se sim, saiba que um log foi gerado e que estamos de olho.')
                TentativaBurla.objects.create(
                    local_deteccao=f'processos_empreendedor:atualizar_documento_processo -> /processos/acompanhamento/{n_protocolo}/requerimento-iss/{doc}/atualizar/',
                    user=request.user,
                    ip_address=request.META.get('REMOTE_ADDR'),
                    informacoes_adicionais=f'Possivel tentativa de acessar arquivo alterando url. Documento não encontrado: {doc}'
                )
                return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)
            if status_doc == '2':
                if request.method == 'POST':
                    # Validar se o arquivo é válido antes de atualizar
                    novo_documento = request.FILES[doc]
                    # Faça a validação necessária, por exemplo, tipo de arquivo, tamanho, etc.
                            
                    with transaction.atomic():
                        # Atualizar o documento
                        if doc in model_to_dict(documentos['iss'].first()):
                            DocumentosRequerimentoISS.objects.filter(requerimento=requerimento_iss).update(**{doc: novo_documento})
                        elif doc in model_to_dict(documentos['sanitaria'].first()):
                            DocumentosLicencaSanitaria.objects.filter(requerimento=requerimento_iss).update(**{doc: novo_documento})
                        elif doc in model_to_dict(documentos['ambiental'].first()):
                            DocumentosLicencaAmbiental.objects.filter(requerimento=requerimento_iss).update(**{doc: novo_documento})
                        else:
                            messages.warning(request, 'Documento não encontrado.')
                            return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)
                        #JUNTAR ESSA PARTE COM A LOGICA DE CIMA
                        # Mudar o status para 'Aguardando avaliação'
                        print(status)
                        print(f"{doc}_status")
                        setattr(status, f"{doc}_status", '0')
                        status.save()

                    # Muda o status para 'Aguardando avaliação'
                    setattr(status, f"{doc}_status", '0')
                    status.save()
                    processo.save()
                    # Verifica se todos os documentos estão aprovados para poder seguir com o processo
                    if processo.tipo_processo.id == 1:
                        is_reprovado = (
                            status.rg_status == '2' or
                            status.comprovante_endereco_status == '2' or
                            status.diploma_ou_certificado_status == '2' or
                            status.licenca_sanitaria == '2' or
                            status.espelho_iptu_status == '2'
                        )
                    elif processo.tipo_processo.id == 3:
                        is_reprovado = (
                            status.contrato_social_status == '2' or
                            status.carteira_orgao_classe_status == '2' or
                            status.alvara_localizacao_status == '2' or
                            status.informacoes_cadastrais_dos_empregados_status == '2' or
                            status.balanco_patrimonial_status == '2' or
                            status.dre_status == '2' or
                            status.balancete_analitico_status == '2' or
                            status.cnpj_copia_status == '2' or
                            status.profissionais_habilitados_status == '2' or
                            status.ir_empresa_status == '2' or
                            status.simples_nacional_status == '2'
                        )
                    # Se não há documento reprovado, o processo pode seguir
                    if not is_reprovado:
                        # Criasse então um novo andamento para o processo
                        Andamento_Processo_Digital.objects.create(
                            processo=processo,              
                            status='aa', 
                            observacao = 'Processo atualizado. Aguardando nova avaliação dos documentos.',
                            servidor = None
                        )            
                        processo.status = 'aa'
                        processo.save()
                        messages.success(request, 'Documento enviado com sucesso! Aguarde a nova avaliação dos documentos.')
                    else:
                        messages.warning(request, 'Documento enviado com sucesso! Termine de atualizar os outros documentos.')
                    return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)
                context={
                    'documento': doc
                }
                return render(request, 'sala_do_empreendedor/processos_digitais/att_documento.html', context)
            messages.warning(request, 'Este arquivo não necessita de alteração.')
            return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)
        except Processo_Digital.DoesNotExist:
            messages.warning(request, 'Processo não encontrado.')
        except StatusDocumentosRequerimentoISS.DoesNotExist:
            messages.warning(request, 'Status de documentos ISS não encontrado.')

        return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)
    messages.warning(request, 'Status de documentos ISS não encontrado.')
    return redirect('processos_empreendedor:middle_acompanhamento_processo', n_protocolo=n_protocolo)


from django.http import JsonResponse
import json
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
import base64
import io
import PyPDF2


@login_required()
@staff_member_required()
def enviarLicenca(request, tipo, n_protocolo):
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    requerimento_iss = RequerimentoISS.objects.get(processo=processo)
    if request.method == 'POST':
        try:
            if tipo == 'agente-ambiental':
                docs=DocumentosLicencaAmbiental.objects.get(requerimento=requerimento_iss)
                docs.licenca_ambiental = request.FILES['licenca']
                docs.save()
                boleto = BoletosRequerimentoISS.objects.get(requerimento=requerimento_iss)
                boleto.status_boleto_ambiental = True
                messages.success(request, 'Licença ambiental enviada com sucesso.')
                # criar_notificacao()
            elif tipo == 'agente-sanitario':
                docs=DocumentosLicencaSanitaria.objects.get(requerimento=requerimento_iss)
                docs.licenca_sanitaria = request.FILES['licenca']
                docs.save()
                boleto = BoletosRequerimentoISS.objects.get(requerimento=requerimento_iss)
                boleto.status_boleto_sanitario = True
                messages.success(request, 'Licença sanitária enviada com sucesso.')
                # criar_notificacao()
            else:
                messages.error(request, 'Tipo de licença inválido.')
                return redirect('processos_empreendedor:acompanhamento_requerimento_iss_agente', tipo=tipo, n_protocolo=n_protocolo)
            messages.success(request, 'Licença enviada com sucesso.')
            return redirect('processos_empreendedor:acompanhamento_requerimento_iss_agente', tipo=tipo, n_protocolo=n_protocolo)
        except Exception as e:
            messages.error(request, f'Erro ao enviar a licença. {e}')        
    return render(request, 'requerimentos_iss/agentes/enviar_licenca.html', {'processo': processo, 'tipo': tipo})

@login_required()
@staff_member_required()
def enviarInscricao(request, tipo, n_protocolo):
    
    if tipo != 'agente-tributario':
        messages.error(request, 'Você não possui permissão para acessar essa página.')
        return redirect('processos_empreendedor:listar_processos')
    
    processo = Processo_Digital.objects.get(n_protocolo=n_protocolo)
    requerimento_iss = RequerimentoISS.objects.get(processo=processo)
    if request.method == 'POST':
        try:                            
            boleto = BoletosRequerimentoISS.objects.get(requerimento=requerimento_iss)
            boleto.boleto_requerimento  = request.FILES['boleto']
            requerimento_iss.n_inscricao = request.POST['n_inscricao']
            boleto.save()
            requerimento_iss.save()
            messages.success(request, 'Boleto e número de inscrição enviados com sucesso.')
            # criar_notificacao()            
            return redirect('processos_empreendedor:acompanhamento_requerimento_iss_agente', tipo=tipo, n_protocolo=n_protocolo)            
        except Exception as e:
            messages.error(request, f'Erro ao enviar as informações. Evite documentos com caracteres especiais. {e}')        
    return render(request, 'requerimentos_iss/agentes/enviar_inscricao.html', {'processo': processo, 'tipo': tipo})

@login_required()
@staff_member_required()
def mudaStatus(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        if data.get('agente') == 'sanitario':
            print('sanitario')
            status_documentos = StatusDocumentosLicencaSanitaria.objects.get(id=data.get('id'))
            setattr(status_documentos, str(data.get('arquivo'))+'_status', str(data.get('status')))
            status_documentos.save()
        elif data.get('agente') == 'ambiental':
            print('ambiental')
            status_documentos = StatusDocumentosLicencaAmbiental.objects.get(id=data.get('id'))
            atributo = str(data.get('arquivo'))+'_status'
            print(atributo, str(data.get('status')))
            teste=setattr(status_documentos, atributo, str(data.get('status')))
            status_documentos.save()
        elif data.get('agente') == 'tributario':
            print('tributario')
            atributo = str(data.get('arquivo'))+'_status'
            print(atributo, str(data.get('status')))
            status_documentos = StatusDocumentosRequerimentoISS.objects.get(id=int(data.get('id')))
            teste=setattr(status_documentos, atributo, str(data.get('status')))
            print(teste)
            status_documentos.save()
        else:
            print('shit')
        return JsonResponse({'status': 'ok'})            
    return JsonResponse({})


@login_required()
@staff_member_required()
def criaRelatorio(request, tipo, n_protocolo):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        try:
            agente = Agente.objects.get(pessoa=Pessoa.objects.get(user=request.user))
            relatorio = Relatorios.objects.create(processo_id=data['processo_id'], user=agente, descricao=data['descricao'])
            print(data['agentes'])
            print(len(data['agentes']))
            if len(data['agentes'])==0:
                relatorio.aprovado = True
            
            relatorio.save()

            for agente_id in data['agentes']:
                AgentesRelatorios.objects.create(
                    relatorio = relatorio,
                    agente = Agente.objects.get(id=agente_id)
                )
            
            return JsonResponse({'status': 'ok', 'nome': str(agente)})            
        except Exception as e:
            print(e)
            pass
    return JsonResponse({})

@login_required()
@staff_member_required()
def buscarAgentes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))   
        if data['pesquisar'] != '':    
            agentes = Agente.objects.filter(pessoa__nome__icontains=data['pesquisar'])

            agentes_list = [{'id': agente.id, 'nome': agente.pessoa.nome} for agente in agentes]
            return JsonResponse({'agentes': agentes_list, 'status': 'ok'})
        return JsonResponse({'status': 'ok', 'agentes': []  })

@login_required
@staff_member_required
@require_POST
def receberBoleto(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        processo_id = data.get('processo_id')
        tipo_boleto = data.get('tipo_boleto')  # 'ambiental' ou 'sanitario'
        boleto_file = data.get('boleto_file')  # Arquivo em base64
        
        if not all([processo_id, tipo_boleto, boleto_file]):
            return JsonResponse({'status': 'error', 'message': 'Dados incompletos'}, status=400)
        
        # Decodificando o arquivo base64
        file_data = ContentFile(base64.b64decode(boleto_file), name=f'{processo_id}_{tipo_boleto}_boleto.pdf')
        
        # Obtenha a instância do RequerimentoISS correspondente ao processo_id
        try:
            requerimento = RequerimentoISS.objects.get(processo__id=processo_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Requerimento não encontrado'}, status=404)
        
        # Obtenha ou crie a instância de BoletosRequerimentoISS associada
        boleto, created = BoletosRequerimentoISS.objects.get_or_create(requerimento=requerimento)
        
        # Salve o arquivo no campo apropriado
        if tipo_boleto == 'ambiental':
            boleto.boleto_licenca_ambiental = file_data
            boleto.status_boleto_ambiental = False # Atualize o status se necessário
        elif tipo_boleto == 'sanitario':
            boleto.boleto_licenca_sanitaria = file_data
            boleto.status_boleto_sanitario = False # Atualize o status se necessário
        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo de boleto inválido'}, status=400)
        
        # Salve a instância de BoletosRequerimentoISS
        boleto.save()
        
        return JsonResponse({'status': 'ok'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@login_required
@staff_member_required
@require_POST
def receberComprovante(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        processo_id = data.get('processo_id')
        tipo_comprovante = data.get('tipo_comprovante')  # 'ambiental' ou 'sanitario'
        comprovante_file = data.get('comprovante_file')  # Arquivo em base64
        
        if not all([processo_id, tipo_comprovante, comprovante_file]):
            return JsonResponse({'status': 'error', 'message': 'Dados incompletos'}, status=400)
        
        # Decodificando o arquivo base64
        file_data = ContentFile(base64.b64decode(comprovante_file), name=f'{processo_id}_{tipo_comprovante}_comprovante.pdf')
        
        # Verificar se o arquivo é um PDF
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_data.read()))
            if len(pdf_reader.pages) == 0:
                return JsonResponse({'status': 'error', 'message': 'Arquivo inválido. O PDF está vazio.'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': 'Arquivo inválido. O arquivo não é um PDF válido.'}, status=400)

        # Obtenha a instância do RequerimentoISS correspondente ao processo_id
        try:
            requerimento = RequerimentoISS.objects.get(processo__id=processo_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Requerimento não encontrado'}, status=404)
        
        # Obtenha ou crie a instância de comprovantesRequerimentoISS associada
        boleto, created = BoletosRequerimentoISS.objects.get_or_create(requerimento=requerimento)
        
        # Salve o arquivo no campo apropriado
        if tipo_comprovante == 'ambiental':
            boleto.comprovante_licenca_ambiental = file_data            
        elif tipo_comprovante == 'sanitario':
            boleto.comprovante_licenca_sanitaria = file_data     
                   
        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo de comprovante inválido'}, status=400)
        
        # Salve a instância de BoletosRequerimentoISS
        boleto.save()
        
        return JsonResponse({'status': 'ok'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
