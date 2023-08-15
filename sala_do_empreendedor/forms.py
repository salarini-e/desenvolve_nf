from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class FormEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = [ 'cnpj', 'nome', 'porte', 'atividade','ramo', 'outro_ramo', 'receber_noticias', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        }