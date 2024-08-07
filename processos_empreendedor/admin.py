from django.contrib import admin
from .models import RequerimentoISS, DocumentosRequerimentoISS, StatusDocumentosRequerimentoISS, DocumentosLicencaAmbiental, StatusDocumentosLicencaAmbiental, DocumentosLicencaSanitaria, StatusDocumentosLicencaSanitaria
from .models import Relatorios, BoletosRequerimentoISS, AgentesRelatorios

# Register your models here.
@admin.register(RequerimentoISS)
class RequerimentoISSAdmin(admin.ModelAdmin):
    list_display = ['processo', 'profissao', 'autonomo_localizado', 'n_inscricao', 'dt_solicitacao', 'dt_atualizacao']
    search_fields = ['processo__n_protocolo']

@admin.register(DocumentosRequerimentoISS)
class DocumentosRequerimentoISSAdmin(admin.ModelAdmin):
    list_display = ['requerimento']
    search_fields = ['requerimento__processo__n_protocolo']

@admin.register(StatusDocumentosRequerimentoISS)
class StatusDocumentosRequerimentoISSAdmin(admin.ModelAdmin):
    list_display = ['requerimento', 'rg_status', 'comprovante_endereco_status', 'diploma_ou_certificado_status', 'espelho_iptu_status']

@admin.register(DocumentosLicencaAmbiental)
class DocumentosLicencaAmbientalAdmin(admin.ModelAdmin):
    list_display = ['requerimento']
    search_fields = ['requerimento__processo__n_protocolo']

@admin.register(StatusDocumentosLicencaAmbiental)
class StatusDocumentosLicencaAmbientalAdmin(admin.ModelAdmin):
    list_display = ['requerimento', 'contrato_locacao_status', 'conta_dagua_status', 'conta_luz_status', 'foto_status', 'croqui_acesso_status']

@admin.register(DocumentosLicencaSanitaria)
class DocumentosLicencaSanitariaAdmin(admin.ModelAdmin):
    list_display = ['requerimento']
    search_fields = ['requerimento__processo__n_protocolo']

@admin.register(StatusDocumentosLicencaSanitaria)
class StatusDocumentosLicencaSanitariaAdmin(admin.ModelAdmin):
    list_display = ['requerimento', 'comprovante_ar_condicionado_status', 'comprovante_limpeza_caixa_dagua_status', 'plano_gerenciamento_de_residuos_status', 'licenca_santinaria_anterior_status']


@admin.register(Relatorios)
class RelatoriosAdmin(admin.ModelAdmin):
    list_display = ['processo']
    search_fields = ['processo__n_protocolo']

@admin.register(BoletosRequerimentoISS)
class BoletosRequerimentoISSAdmin(admin.ModelAdmin):
    list_display = ['requerimento']
    search_fields = ['requerimento__processo__n_protocolo']

@admin.register(AgentesRelatorios)
class AgentesRelatoriosAdmin(admin.ModelAdmin):
    list_display = ['relatorio', 'agente']
    search_fields = ['relatorio__processo__n_protocolo']