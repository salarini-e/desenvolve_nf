from django import forms
from .models import CadastroPCA

class CadastroPCAForm(forms.ModelForm):
    class Meta:
        model = CadastroPCA
        fields = [
            'user',
            'orgao_requisitante',
            'subsecretaria_departamento',
            'celular_whatsapp',
            'email',
            'objeto_licitacao',
            'registro_preco',
            'prazo_execucao',
            'data_prevista_certame',
            'fonte_recurso',
            'origem_preco_referencia',
            'ata_registro',
            'outro'
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'orgao_requisitante': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'subsecretaria_departamento': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'celular_whatsapp': forms.TextInput(attrs={'class': 'form-control mb-3', 'onkeyup': 'mascara(this, itel)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'objeto_licitacao': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 4}),
            'registro_preco': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'prazo_execucao': forms.TextInput(attrs={'class': 'form-control mb-3', 'onkeyup': 'mascara(this, iprazo)'}),
            'data_prevista_certame': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'mm/aaaa', 'onkeyup': 'validateDate(this)'}),
            'fonte_recurso': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'origem_preco_referencia': forms.Select(attrs={'class': 'form-select mb-3', 'onchange': 'toggleFields()'}),
            'ata_registro': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'outro': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        origem_preco_referencia = cleaned_data.get("origem_preco_referencia")
        ata_registro = cleaned_data.get("ata_registro")
        outro = cleaned_data.get("outro")

        # Validação personalizada
        if origem_preco_referencia == CadastroPCA.ATA_REGISTRO and not ata_registro:
            self.add_error('ata_registro', "Este campo é obrigatório quando 'Ata de Registro' for selecionado.")
        
        if origem_preco_referencia == CadastroPCA.OUTRO and not outro:
            self.add_error('outro', "Este campo é obrigatório quando 'Outro' for selecionado.")