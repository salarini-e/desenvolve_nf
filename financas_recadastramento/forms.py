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


class _PessoaRecadastramentoForm(forms.ModelForm):
    class Meta:
        model = PessoaRecadastramento
        fields = [
            'cpf', 'responsavel_tributario', 'cnpj', 'nome_do_contribuinte', 'celular', 'cep',
            'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'email'
        ]
        widgets = {
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '14',
                'id': 'id_cpf',
                'onkeyup': 'mascara(this, icpf)',
                'onblur': 'checkCPF(this.value)'
            }),
            'responsavel_tributario': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '150',
                'id': 'id_responsavel_tributario',
                'required': 'required'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '14',
                'id': 'id_cnpj'
            }),
            'nome_do_contribuinte': forms.TextInput(attrs={
                'class': 'form-control text-capitalize',
                'maxlength': '150',
                'id': 'id_nome_do_contribuinte',
                'required': 'required'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '15',
                'id': 'id_celular'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '9',
                'id': 'id_cep',
                'onkeydown': 'icep(this)',
                'onblur': 'getCEP(this)'
            }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control text-capitalize',
                'maxlength': '150',
                'id': 'id_rua'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '10',
                'id': 'id_numero'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '50',
                'id': 'id_complemento'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control text-capitalize',
                'maxlength': '50',
                'id': 'id_bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control text-capitalize',
                'maxlength': '50',
                'id': 'id_cidade'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control text-capitalize',
                'maxlength': '2',
                'id': 'id_estado'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'maxlength': '254',
                'id': 'id_email'
            }),
        }

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['requerente', 'requerimento', 'ano', 'localizacao']
        widgets = {
            'requerente': forms.Select(attrs={'class': 'form-control'}),
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
