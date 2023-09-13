#Form para solicitacao de cadastro de camera usando o modelo solicitacao_de_cadastro_de_camera

from django import forms
from .models import Solicitacao_de_cadastro_de_camera

class Solicitacao_de_cadastro_de_cameraForm(forms.ModelForm):
    class Meta:
        model = Solicitacao_de_cadastro_de_camera
        exclude = ['dt_inclusao', 'atendido']
        widgets = {
            'pessoa': forms.HiddenInput(),
            'autorizacao': forms.RadioSelect(),
            'tipo_camera': forms.RadioSelect(),
            'informacoes_de_acesso': forms.RadioSelect(),
        }