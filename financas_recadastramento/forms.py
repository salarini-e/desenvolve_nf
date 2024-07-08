from django import forms
from .models import PessoaRecadastramento, Processo, Inscricao

class PessoaRecadastramentoForm(forms.ModelForm):
    class Meta:
        model = PessoaRecadastramento
        fields = [
            'cpf', 'responsavel_tributario', 'cnpj', 'nome_do_contribuinte', 'celular', 'cep', 'rua',
            'numero', 'complemento', 'bairro', 'cidade', 'estado', 'email'
        ]
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'onkeyup': 'console.log(this.value)'}),
            'responsavel_tributario': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_do_contribuinte': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['pessoa_recadastramento', 'requerente', 'requerimento', 'ano', 'localizacao']
        widgets = {
            'pessoa_recadastramento': forms.Select(attrs={'class': 'form-control'}),
            'requerente': forms.TextInput(attrs={'class': 'form-control'}),
            'requerimento': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['pessoa_recadastramento', 'numero_inscricao']
        widgets = {
            'pessoa_recadastramento': forms.Select(attrs={'class': 'form-control'}),
            'numero_inscricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
