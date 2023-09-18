from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class FormEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = [ 'cnpj', 'nome', 'porte', 'atividade','ramo', 'outro_ramo','telefone', 'whatsapp', 'email', 'site', 'descricao',  'receber_noticias']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ', 'onkeydown':'mascara(this, icnpj)'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'onkeydown':'mascara(this, itel)'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp', 'onkeydown':'mascara(this, itel)'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'atividade': forms.CheckboxSelectMultiple(),
            'ramo': forms.CheckboxSelectMultiple(),
        }
        
class FormAlterarEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'porte', 'atividade','ramo', 'outro_ramo', 'telefone', 'whatsapp', 'email', 'site', 'descricao', 'receber_noticias']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'onkeydown':'mascara(this, itel)'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp', 'onkeydown':'mascara(this, itel)'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        }
        
class FormLogoEmpresa(ModelForm):
    class Meta:
        model = Registro_no_vitrine_virtual
        fields = ['logo']

class FormCadastrarProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['imagem', 'nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        }
        
class Faccao_Legal_Form(ModelForm):
    class Meta:
        model = Faccao_legal
        widgets={
         'possui_cnpj': forms.RadioSelect(attrs={'class': 'form-check-input', 'onclick': 'mostrar_cnpj(toggleCnpjDiv(this))'}),   
         'user': forms.HiddenInput(),
         'trabalha_com': forms.CheckboxSelectMultiple(),
         'equipamentos': forms.CheckboxSelectMultiple(),
         'tipo_produto': forms.CheckboxSelectMultiple(),
        }
        exclude = []