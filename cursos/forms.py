
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


class CadastroCandidatoForm(ModelForm):

    class Meta:
        model = Aluno
        widgets = {
            'turmas': forms.CheckboxSelectMultiple(),
            'celular': forms.TextInput(attrs={'onkeydown': 'mascara(this, icelular)'}),
            'cep': forms.TextInput(attrs={'onkeydown': 'mascara(this, icep)'}),
            'cpf': forms.TextInput(attrs={'onkeydown': 'mascara(this, icpf)'}),
            'rg': forms.TextInput(attrs={'onkeydown': 'mascara(this, irg)'}),
            'dt_nascimento': forms.TextInput(attrs={'type': 'date'}),
            'aceita_mais_informacoes': forms.CheckboxInput(attrs={'required': True}),
            'dt_nascimento': forms.widgets.DateInput(attrs={'type': 'date'}),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
        }
        exclude = ['dt_inclusao', 'dt_alteracao', 'li_e_aceito_termos']


class CadastroProfessorForm(ModelForm):

    class Meta:
        model = Instrutor
        widgets = {
            'cpf': forms.TextInput(attrs={'onkeydown': 'mascara(this, icpf)'}),
            'celular': forms.TextInput(attrs={'onkeydown': 'mascara(this, icelular)'}),
        }
        exclude = ['dt_inclusao']


class CadastroCursoForm(ModelForm):

    class Meta:
        model = Curso
        widgets = {
            'categoria': forms.HiddenInput(),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
            'dt_nascimento': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['dt_inclusao', 'dt_alteracao']


class CadastroCursoForm2(ModelForm):

    class Meta:
        model = Curso
        widgets = {
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
        }
        exclude = ['dt_inclusao', 'dt_alteracao']


class CadastroTurmaForm(ModelForm):

    class Meta:
        model = Turma
        widgets = {
            'curso': forms.Select(attrs={'oninput': 'getCandidatos(this)'}),
            'data_inicio': forms.TextInput(attrs={'type': 'date'}),
            'data_final': forms.TextInput(attrs={'type': 'date'}),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
            'instrutor': forms.CheckboxSelectMultiple()
        }
        exclude = ['dt_inclusao', 'dt_alteracao']


class CadastroCategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        exclude = []


class CadastroLocalForm(ModelForm):

    class Meta:
        model = Local
        widgets = {
            'ativo': forms.HiddenInput(),
            'cep': forms.TextInput(attrs={'onkeydown': 'mascara(this, icep)'}),
        }
        exclude = []


class CadastroAlunoForm(ModelForm):

    class Meta:
        model = Aluno
        widgets = {
            'celular': forms.TextInput(attrs={'onkeydown': 'mascara(this, icelular)'}),
            'dt_nascimento': forms.TextInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'onkeydown': 'mascara(this, icpf)'}),

        }
        exclude = []


class CadastroResponsavelForm(ModelForm):

    class Meta:
        model = Responsavel
        widgets = {
            'celular': forms.TextInput(attrs={'onkeydown': 'mascara(this, icelular)'}),
            'dt_nascimento': forms.TextInput(attrs={'type': 'date'}),
            'cep': forms.TextInput(attrs={'onkeydown': 'mascara(this, icep)'}),
            'rg': forms.TextInput(attrs={'onkeydown': 'mascara(this, irg)'}),
            'cpf': forms.TextInput(attrs={'onkeydown': 'mascara(this, icpf)'}),

        }
        exclude = ['aluno']

class Instituicao_form(ModelForm):

    class Meta:
        model = Instituicao
        exclude = []