from financas.models import *
from django import forms

class ConselheirosForm(forms.ModelForm):
    class Meta:
        model = Conselheiros
        fields = '__all__'  
        widgets = {       
            'user_inclusao': forms.HiddenInput(),
            'ativo': forms.HiddenInput()
        }

class Pauta_de_JulgamentoForm(forms.ModelForm):
    class Meta:
        model = Pauta_de_Julgamento
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'user_inclusao': forms.HiddenInput(),
            'ativo': forms.HiddenInput()
        }

class SumulasForm(forms.ModelForm):
    class Meta:
        model = Sumulas
        exclude =['dt_inclusao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'user_inclusao': forms.HiddenInput(),
            'ativo': forms.HiddenInput()
        }

class AcordaoForm(forms.ModelForm):
    class Meta:
        model = Acordao
        exclude =['dt_inclusao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'user_inclusao': forms.HiddenInput(),
            'ativo': forms.HiddenInput()
        }

class AtaForm(forms.ModelForm):
    class Meta:
        model = Ata
        exclude =['dt_inclusao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'user_inclusao': forms.HiddenInput(),
            'ativo': forms.HiddenInput()
        }

class Voto_RelatorForm(forms.ModelForm):
    class Meta:
        model = Voto_Relator
        exclude =['dt_inclusao']
        widgets = {
            'user_inclusao': forms.HiddenInput()
        }

