from django import forms
from django.forms import ModelForm, ValidationError
from .models import OrdemDeServico, Funcionario_OS, OS_ext, OS_Linha_Tempo


class OS_Form(ModelForm):    
    
    class Meta:
        model = OrdemDeServico
        widgets = {
            'tipo': forms.Select(attrs={'readonly': True}),
        }
        exclude = ['numero', 'dt_inclusao', 'atendente', 'dt_conclusao', 'prioridade', 'status', 'contribuinte', 'pontos_atendidos', 'cadastrado_por']

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

class NovaMensagemForm(forms.ModelForm):
    class Meta:
        model = OS_Linha_Tempo
        fields = ['os', 'pessoa', 'mensagem', 'anexo']
        widgets = {
            'os': forms.HiddenInput(),
            'pessoa': forms.HiddenInput(),
            'mensagem': forms.Textarea(attrs={'class': 'form-control h-100', 'rows': 6}),
            'anexo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }