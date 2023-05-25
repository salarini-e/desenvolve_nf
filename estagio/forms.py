from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


class Estudante_form(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(Estudante_form, self).__init__(*args, **kwargs)
    #     self.fields['universidade'].queryset = Universidade.objects.all()
    #     self.fields['curso'].queryset = Curso.objects.all()

    #     print(self.instance, 'AQUI')
       
    #     if self.instance:  # Verifica se existe uma instância do modelo
    #             self.fields['universidade'].initial = self.instance.universidade.id
    #             self.fields['curso'].initial = self.instance.curso.id

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

        #tem que verificar ao salvar se ja n existe uma relacao do estudante com a vaga
        
        exclude = ['data_inclusao', 'data_fim', 'data_inicio', 'supervisor']