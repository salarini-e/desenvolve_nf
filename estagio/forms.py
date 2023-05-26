from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


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
        print("Campo 'curso da vaga':", vaga.curso.all())
        print("Campo 'curso do estudante':", estudante.curso)
        if estudante.curso in vaga.curso.all():
            return True
        self.add_error('vaga', "O seu curso não corresponde com o da vaga! Tente outro.")    
        return False
        