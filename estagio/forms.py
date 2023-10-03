from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class Date(forms.DateInput):
    input_type = 'date'

class Estudante_form(ModelForm):
    
    def __init__(self, *args, **kwargs):
        print(args)
        initial = kwargs.get('initial', {})
        universidade_id = initial.get('universidade', None)

        super(Estudante_form, self).__init__(*args, **kwargs)
        # Aqui você pode popular as opções do campo universidade e curso
        if universidade_id is not None:
            self.fields['curso'].choices = [(curso.id, curso.nome) for curso in Curso.objects.filter(universidade_id=universidade_id)]
        elif self.is_bound and 'universidade' in self.data:
        # Verifica se o formulário está vinculado (método POST) e se 'universidade' está presente nos dados POST
            post_universidade_id = self.data['universidade']
            self.fields['curso'].choices = [(curso.id, curso.nome) for curso in Curso.objects.filter(universidade_id=post_universidade_id)]
   
    class Meta:
        model = Estudante
        widgets = {
            'pessoa':forms.HiddenInput(),
            'universidade': forms.Select(attrs={'class':'form-control', 'onchange':'get_cursos(this.value)', 'readonly': 'readonly'}),
            'curso': forms.Select(attrs={'class':'form-control', 'onchange':'checkVaga(this)'}),
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

class Estudante_TCE_form(ModelForm):
    class Meta:
        model = Estudante_Vaga
        widgets = {
            'TCE': forms.FileInput(attrs={'class':'form-control'}),
        }
        exclude = ['estudante', 'vaga', 'status', 'data_inclusao', 'data_fim', 'data_inicio', 'supervisor', 'local_do_estagio', 'universidade', 'matricula', 'local_do_estagio_de_pretensao']
        
class Estudante_vaga_form(ModelForm):
    class Meta:
        model = Estudante_Vaga
        widgets = {
            'estudante':forms.HiddenInput(),
            # 'vaga': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }
        exclude = ['data_inclusao', 'data_fim', 'data_inicio', 'supervisor', 'local_do_estagio', 'universidade', 'matricula', 'TCE']   

    def is_valid(self, estudante):
        valid = super().is_valid()
        # print(self.cleaned_data['local_do_estagio_de_pretensao'])
        local=Locais_de_Estagio.objects.get(id=self.cleaned_data['local_do_estagio_de_pretensao'].id)
        try:
            tem_estagio=Estudante_Vaga.objects.get(estudante=estudante, status='1')
        except:
            tem_estagio=False

        if tem_estagio:
            self.add_error('local_do_estagio_de_pretensao', "Você já está estagiando! É necessario concluir o estagio para se candidatar novamente.")    
            return False
        
        try:
            jaehcandidato=Estudante_Vaga.objects.get(estudante=estudante, local_do_estagio_de_pretensao=local, status='0')
        except:
            jaehcandidato=False
        
        if jaehcandidato:
            self.add_error('local_do_estagio_de_pretensao', "Você já se candidatou a essa vaga.")    
            return False
        else:
            cursos = local.cursos.all()
            # teste_valid = []
            print(estudante.curso)
            print(cursos)
            if estudante.curso in cursos:
                return True
            else:
                self.add_error('local_do_estagio_de_pretensao', "Você não pode se candidatar a essa vaga pois seu curso não é compativel.")                    
                return False
                    
            # for teste in teste_valid:
            #     if teste:
            #        return True
            #     else:
            #         self.add_error('local_do_estagio_de_pretensao', "Você não pode se candidatar a essa vaga pois seu curso não é compativel.")                    
            #         return False

                
class Cadatrar_Vaga_form(ModelForm):
    class Meta:
        model = Vagas
        exclude = []

class Editar_Vaga_form(ModelForm):
    class Meta:
        model = Vagas
        exclude = ['data_inclusao']
        
class Supervisor_form(ModelForm):
    class Meta:
        model = Supervisor
        exclude = ['data_inclusao']

class Secretaria_form(ModelForm):
    class Meta:
        model = Secretaria
        exclude = ['data_inclusao']

class Local_form(ModelForm):
    class Meta:
        model = Locais_de_Estagio
        widgets = {
            'secretaria':forms.HiddenInput()
        }
        exclude = []

class Editar_Curso_forms(ModelForm):

    class Meta:
        model = Curso
        widgets = {
            
        }
        
        exclude = ['data_inclusao', 'universidade']

class Editar_Supervisor_forms(ModelForm):

    class Meta:
        model = Supervisor
        widgets = {
            
        }
        
        exclude = ['data_inclusao', 'pessoa']
        
class Form_locais_adicionar_ou_remover_cursos(ModelForm):
    
        class Meta:
            model = Locais_de_Estagio
            widgets = {
                'cursos': forms.CheckboxSelectMultiple(),
            }            
            exclude = ['data_inclusao', 'secretaria', 'local', 'bairro', 'telefone_responsavel', 'telefone_local', 'quantidade_maxima']
    