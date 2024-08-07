from django import forms
from django.forms import ModelForm, ValidationError
from ..models import *


class Processo_ISS_Form(ModelForm):
    class Meta:
        model = RequerimentoISS
        widgets = {
            'profissao': forms.RadioSelect(),
            'solicitante': forms.HiddenInput(),
            'n_inscricao': forms.HiddenInput(),        
            }
        exclude = ['processo', 'dt_solicitacao', 'boleto', 'boleto_pago', 'status', 'boleto_meio_ambiente', 'boleto_meio_ambiente_status', 'boleto_saude', 'boleto_saude_status']

class Documentos_ISS_Form(ModelForm):
    class Meta:
        model = DocumentosRequerimentoISS
        widgets = {
            'rg': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'comprovante_endereco': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'diploma_ou_certificado': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'espelho_iptu': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        exclude = ['requerimento']

class Documentos_ISS_SEM_DIPLOMA_Form(ModelForm):
    class Meta:
        model = DocumentosRequerimentoISS
        widgets = {
            'rg': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'comprovante_endereco': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),            
            'espelho_iptu': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        exclude = ['requerimento', 'diploma_ou_certificado']

        

class DocumentosLicencaAmbiental_Form(ModelForm):
    class Meta:
        model = DocumentosLicencaAmbiental
        widgets = {
            'contrato_locacao': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'conta_dagua': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'croqui_acesso': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        exclude = ['requerimento','licenca_ambiental']

class DocumentosLicencaSanitaria_Form(ModelForm):
    class Meta:
        model = DocumentosLicencaSanitaria
        widgets = {
            'comprovante_ar_condicionado': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'comprovante_limpeza_caixa_dagua': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'plano_gerenciamento_de_residuos': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'licenca_sanitaria': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            }
        exclude = ['requerimento', 'licenca_sanitaria']
# class Criar_Processo_Docs_Form(ModelForm):
#     class Meta:
#         model = Processo_Status_Documentos_Anexos
#         widgets = {
#             'processo': forms.HiddenInput(),
#             }
        
#         exclude = ['user_register', 'rg_status', 'licenca_sanitaria',
#                    'comprovante_endereco_status', 'diploma_ou_certificado_status', 
#                    'licenca_sanitaria_status', 'espelho_iptu_status', 
#                    'licenca_ambiental_status', 'comprovante_limpeza_caixa_dagua_status',
#                    'comprovante_ar_condicionado_status', 'plano_gerenciamento_de_residuos_status', 
#                    'licenca_santinaria_anterior_status', 'agente_att_caixa_dagua', 
#                    'agente_att_ar', 'agente_att_residuos', 'agente_att_licenca_sanitaria_anterior', 
#                    'agente_att_rg', 'agente_att_endereco', 'agente_att_certificado', 
#                    'agente_att_iptu', 'espelho_iptu_status', 'contrato_locacao_status',
#                    'conta_dagua_status', 'conta_luz_status', 'foto_status',
#                    'croqui_acesso_status' ]
                   