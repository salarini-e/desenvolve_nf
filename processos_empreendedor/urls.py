from django.urls import path
from . import views
 
app_name='processos_empreendedor'
urlpatterns = [
    path('novo/', views.novo_processo, name='novo_processo'),

    path('requerimento-iss/', views.requerimento_iss, name='requerimento_iss'),
    path('requerimento-iss/<n_protocolo>/enviar-documentos/', views.requerimento_iss_upload_documentos, name='requerimento_iss_upload'),
    path('consultar/', views.listar_processos, name='listar_processos'),
    path('consultar/<tipo>/', views.listar_processos_agente, name='listar_processos_agente'),
    
    path('acompanhamento/<n_protocolo>/', views.middle_acompanhamento_processo, name='middle_acompanhamento_processo'),
    path('acompanhamento/<n_protocolo>/requerimento-iss/', views.acompanhamento_requerimento_iss, name='acompanhamento_requerimento_iss'),
    
    path('acompanhamento/<tipo>/<n_protocolo>/', views.middle_acompanhamento_processo_agente, name='middle_acompanhamento_processo_agente'),
    path('acompanhamento/<tipo>/<n_protocolo>/requerimento-iss/', views.acompanhamento_requerimento_iss_agente, name='acompanhamento_requerimento_iss_agente'),
    path('acompanhamento/<tipo>/<n_protocolo>/requerimento-iss/notificar/', views.notificar_situacao_documentos, name='notificar_situacao_documentos'),
    
    path('acompanhamento/<tipo>/<n_protocolo>/enviar-licenca/', views.enviarLicenca, name='enviar_licenca'),
    path('acompanhamento/<tipo>/<n_protocolo>/enviar-inscricao/', views.enviarInscricao, name='enviar_inscricao'),
    path('acompanhamento/<tipo>/<n_protocolo>/enviar-relatorio/', views.criaRelatorio, name='enviar_relatorio'),

    path('acompanhamento/<n_protocolo>/requerimento-iss/<doc>/atualizar/', views.atualizar_documento, name='atualizar_documento_processo'),

    path('api/pesquisar-agentes/', views.buscarAgentes, name='pesquisarAgentes'),
    path('api/muda-status/', views.mudaStatus, name='mudaStatus'),
    path('api/receber-boleto/', views.receberBoleto, name='receber_boleto'),
    path('api/receber-comprovante/', views.receberComprovante, name='receber_comprovante'),
]