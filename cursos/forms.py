
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroCandidatoForm(ModelForm):    
    
    class Meta:
        model = Candidato
        widgets = {
            'curso': forms.Select(attrs={'tabindex':'-1', 'aria-disabled':True}),
            'user_inclusao': forms.HiddenInput(),
            'user_ultima_alteracao': forms.HiddenInput(),
        }
        exclude = ['dt_inclusao', 'dt_alteracao']

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

        exclude = []
