
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroCandidatoForm(ModelForm):    
    
    class Meta:
        model = Candidato
        widgets = {
            'turmas': forms.CheckboxSelectMultiple(),
            'celular': forms.TextInput(attrs={'onkeydown':'mascara(this, icelular)'}),
            'cep': forms.TextInput(attrs={'onkeydown':'mascara(this, icep)'}),
            'cpf': forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
            'rg': forms.TextInput(attrs={'onkeydown':'mascara(this, irg)'}),
            'aceita_mais_informacoes': forms.CheckboxInput(attrs={'required':True}),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
        }
        exclude = ['dt_inclusao', 'dt_alteracao', 'turmas_selecionado', 'turmas', 'li_e_aceito_termos']

class CadastroProfessorForm(ModelForm):    
    
    class Meta:
        model = Professor
        widgets = {
            'cpf': forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
            'celular': forms.TextInput(attrs={'onkeydown':'mascara(this, icelular)'}),
        }
        exclude = ['dt_inclusao']


class CadastroCursoForm(ModelForm):    
    
    class Meta:
        model = Curso
        widgets = {          
            'categoria': forms.HiddenInput(),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
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
            'curso': forms.Select(attrs={'onchange':'getCandidatos(this)'}),      
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
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
            'cep': forms.TextInput(attrs={'onkeydown':'mascara(this, icep)'}),
        }
        exclude = []

class CadastroAlunoForm(ModelForm):    
    
    class Meta:
        model = Aluno
        # widgets = {                
        #     'ativo': forms.HiddenInput(),
        # }
        exclude = []

class CadastroResponsavelForm(ModelForm):

    class Meta:
        model = Responsavel
        widgets = {

        }
        exclude = ['r_aluno']