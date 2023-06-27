from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class Date(forms.DateInput):
    input_type = 'date'

class Estudante_form(ModelForm):
    class Meta:
        model = Estudante
        widgets = {
            'pessoa':forms.HiddenInput(),
        }
        
        exclude = ['data_inclusao']

class Universidade_form(ModelForm):
    class Meta:
        model = Universidade
        exclude = ['data_inclusao']

class Universidade_local_form(ModelForm):
    class Meta:
        model = Locais_de_Estagio
        
        exclude = ['data_inclusao']

class Curso_form(ModelForm):
    class Meta:
        model = Curso
        widgets = {
            'universidade': forms.HiddenInput(),
        }
        exclude = ['data_inclusao']

class Editar_estudante_forms(ModelForm):

    class Meta:
        model = Estudante_Vaga
        widgets = {
            'data_inicio': Date(),
            'data_fim': Date(),
        }
        
        exclude = []

class Processo_estudante_forms(ModelForm):

    class Meta:
        model = Processo       
        widgets = {
            'estudante_vaga': forms.HiddenInput()
        }
        exclude = ['n_processo']

class Historico_processo_estudante_forms(ModelForm):

    class Meta:
        model = Historico_Processo
        widgets = {
            'processo': forms.HiddenInput()
        }
        exclude = []

class Estudante_vaga_form(ModelForm):
    class Meta:
        model = Estudante_Vaga
        widgets = {
            'estudante':forms.HiddenInput(),
            'vaga': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }
        exclude = ['data_inclusao', 'data_fim', 'data_inicio', 'supervisor', 'local_do_estagio']   

    def is_valid(self, estudante):
        valid = super().is_valid()
        vaga=Vagas.objects.get(nome=self.cleaned_data['vaga'])
        try:
            tem_estagio=Estudante_Vaga.objects.get(estudante=estudante, status='1')
        except:
            tem_estagio=False

        if tem_estagio:
            self.add_error('vaga', "Você já está estagiando! É necessario concluir o estagio para se candidatar novamente.")    
            return False
        
        try:
            jaehcandidato=Estudante_Vaga.objects.get(estudante=estudante, vaga=vaga, status='0')
        except:
            jaehcandidato=False
        
        if jaehcandidato:
            self.add_error('vaga', "Você já se candidatou a essa vaga.")    
            return False
        else:
            if estudante.curso == vaga.curso:
                if valid:                    
                    return True
            else:
                self.add_error('vaga', "O seu curso não corresponde com o da vaga! Tente outro.")        
                return False
                
class Cadatrar_Vaga_form(ModelForm):
    class Meta:
        model = Vagas
        exclude = []

class Supervisor_form(ModelForm):
    class Meta:
        model = Supervisor
        exclude = ['data_inclusao']

class Secretaria_form(ModelForm):
    class Meta:
        model = Secretaria
        exclude = ['data_inclusao']

class Editar_Curso_forms(ModelForm):

    class Meta:
        model = Curso
        widgets = {
            
        }
        
        exclude = ['data_inclusao', 'universidade']