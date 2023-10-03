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
        #  'possui_mei': forms.RadioSelect(attrs={'class': 'form-check-input', 'onclick': 'toggleCnpjDiv(this)'}),  
        'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ', 'onkeydown':'mascara(this, icnpj)', 'onblur': 'checkCNPJ(icnpj(this.value))'}),
         'user': forms.HiddenInput(),
         'tempo_que_trabalha': forms.RadioSelect(),
         'trabalha_com': forms.CheckboxSelectMultiple(),
         'equipamentos': forms.CheckboxSelectMultiple(),
         'tempo_que_trabalha': forms.RadioSelect(),
         'area': forms.RadioSelect(),   
         'tamanho_area': forms.RadioSelect(),
         'tipo_produto': forms.CheckboxSelectMultiple(),
         'situacao_trabalho': forms.RadioSelect(),
         'situacao_remuneracao': forms.RadioSelect(),
        }
        fields = ['tempo_que_trabalha', 'trabalha_com', 'equipamentos', 'area', 'tamanho_area', 'possui_colaboradores', 'qtd_colaboradores', 'tipo_produto', 'outro_produto', 'situacao_trabalho', 'situacao_remuneracao', 'user', 'possui_mei', 'cnpj', 'qual_seu_sonho_no_setor']
        exclude = []

class Criar_Processo_Admin_Form(ModelForm):
    class Meta:
        model = Processo_Digital
        widgets = {
            'tipo_processo': forms.HiddenInput(),
            'n_protocolo': forms.HiddenInput(),
            'profissao': forms.RadioSelect(),
            'solicitante': forms.HiddenInput(),        
            }
        exclude = ['dt_solicitacao', 'boleto', 'boleto_pago']
        
class Criar_Processo_Form(ModelForm):
    class Meta:
        model = Processo_Digital
        widgets = {
            'tipo_processo': forms.HiddenInput(),
            'n_protocolo': forms.HiddenInput(),
            'profissao': forms.RadioSelect(),
            'solicitante': forms.HiddenInput(),        
            }
        exclude = ['dt_solicitacao', 'boleto', 'boleto_pago', 'status']
               
class Criar_Andamento_Processo(ModelForm):
    class Meta:
        model = Andamento_Processo_Digital
        widgets = {
            'processo': forms.HiddenInput(),
            'servidor': forms.HiddenInput(),
            }
        exclude = ['dt_andamento']