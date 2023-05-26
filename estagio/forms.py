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

class Editar_estudante_forms(ModelForm):

    class Meta:
        model = Estudante_Vaga
        widgets = {
            'data_inicio': Date(),
            'data_fim': Date(),
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
        exclude = ['data_inclusao', 'data_fim', 'data_inicio', 'supervisor']   

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
            if estudante.curso in vaga.curso.all():
                if valid:
                    return True
            else:
                self.add_error('vaga', "O seu curso não corresponde com o da vaga! Tente outro.")        
                return False
        