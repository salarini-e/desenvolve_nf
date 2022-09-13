
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroCandidatoForm(ModelForm):    
    
    class Meta:
        model = Candidato
        widgets = {
            'turmas': forms.CheckboxSelectMultiple(),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
        }
        exclude = ['dt_inclusao', 'dt_alteracao', 'turmas_selecionado', 'turmas', 'li_e_aceito_termos']

class CadastroProfessorForm(ModelForm):    
    
    class Meta:
        model = Professor
        exclude = ['dt_inclusao']


class CadastroCursoForm(ModelForm):    
    
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
        }
        exclude = []

class CadastroAlunoForm(ModelForm):    
    
    class Meta:
        model = Aluno
        # widgets = {                
        #     'ativo': forms.HiddenInput(),
        # }
        exclude = []
