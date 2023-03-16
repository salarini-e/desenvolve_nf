from django import forms
from django.forms import ModelForm, ValidationError
from .models import OrdemDeServico, Funcionario_OS, OS_ext


class OS_Form(ModelForm):    
    
    class Meta:
        model = OrdemDeServico
        # widgets = {                
        #     'cpf': forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
        #     'telefone': forms.TextInput(attrs={'onkeydown':'mascara(this, itel)'})
        # }
        exclude = ['numero', 'dt_inclusao', 'atendente', 'dt_conclusao', 'prioridade', 'status', 'contribuinte']

class Funcionario_Form(ModelForm):
    class Meta:
        model = Funcionario_OS
        fields = ['pessoa', 'tipo_os']

class Equipe_Form(ModelForm):
    class Meta:
        model = OS_ext
        widgets = {
            'equipe': forms.CheckboxSelectMultiple(),
            'os': forms.HiddenInput()

        }        
        exclude=[]