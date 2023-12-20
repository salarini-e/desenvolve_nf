import random
import string
from django.db import models
from autenticacao.models import Pessoa
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator


class Universidade(models.Model):    
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    nome_responsavel = models.CharField(max_length=150, verbose_name="Nome do responsável de estágio da instituição")
    contato = models.CharField(max_length=50, verbose_name="Contato do responsável de estágio da instituição")
    logo = models.ImageField(upload_to = 'estagio/media/logo_universidade/', null=True, blank=True)
    dt_inicio_do_termo = models.DateField(null=True, blank=True)
    dt_vencimento_do_termo = models.DateField(null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    ativa = models.BooleanField(default=True)
    def __str__(self):
         return '%s' % (self.nome)

class Responsavel_Universidade(models.Model):
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20, default='Cargo do Responsável')
    email_institucional = models.EmailField()
    telefone_institucional = models.CharField(max_length=15, verbose_name='Telefone', null=True)

    def __str__(self):
         return '%s - %s' % (self.pessoa.nome, self.universidade.nome)
    
class Curso(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do curso")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    universidade = models.ForeignKey(Universidade, on_delete= models.CASCADE)
   
    def __str__(self):
         return '%s - %s' % (self.nome, self.universidade.nome)
   
class Secretaria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da secretaria")    
    telefone = models.CharField(max_length=15, verbose_name='Telefone da secretaria', null=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    
    def __str__(self):
        return self.nome

class Locais_de_Estagio(models.Model):
    secretaria =  models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, verbose_name="Nome do local")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    telefone_responsavel = models.CharField(max_length=15, verbose_name='Telefone do responsável do local', null=True)
    telefone_local = models.CharField(max_length=15, verbose_name='Telefone do local', null=True)    
    quantidade_maxima = models.IntegerField()
    cursos = models.ManyToManyField(Curso)
    def __str__(self):
        return '%s - %s' % (self.local, self.local)

class Vagas(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome vagas")
    descricao = models.TextField(blank=True, null=True)
    quantidade_de_vagas = models.IntegerField(verbose_name="Quantidade de vagas")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    img = models.ImageField(upload_to = 'estagio/media/banner_vagas/', null=True)
    img2 = models.ImageField(upload_to = 'estagio/media/banner_vagas/', null=True)
    secretaria = models.ManyToManyField(Secretaria)
    curso = models.ManyToManyField(Curso)
    locais = models.ManyToManyField(Locais_de_Estagio)
    quantidade_maxima = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Supervisor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, verbose_name="Nome supervisor")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    secretaria = models.ForeignKey(Secretaria, on_delete= models.CASCADE)
    n_vagas = models.IntegerField(verbose_name="Número de vagas")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    celular =models.CharField(max_length=15, verbose_name="Celular", null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Vaga_Supervisor(models.Model): 
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vaga     + ' - ' + self.pessoa

class Estudante(models.Model):
    pessoa = models.ForeignKey(Pessoa, related_name='aluno_pessoa', on_delete=models.PROTECT)
    matricula = models.CharField(max_length=50, verbose_name= "Sua matricula")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    universidade = models.ForeignKey(Universidade, on_delete=models.RESTRICT, verbose_name='Sua universidade atual')
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Seu curso')
    
    def __str__(self):
        return self.pessoa.nome
    
class Estudante_Vaga(models.Model):
    STATUS_CHOICES = (
        ('0', 'Candidato'),
        ('1', 'Estagiando'),
        ('2', 'Estágio concluído'),
        ('3', 'Candidatura cancelada')
    )
    universidade = models.ForeignKey(Universidade, on_delete=models.RESTRICT, blank=True, null=True)
    matricula = models.CharField(max_length=50, verbose_name= "Sua matricula", blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status', default=0)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)        
    # vaga = models.ForeignKey(Vagas, on_delete=models.RESTRICT)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.RESTRICT, blank=True, null=True)
    estudante = models.ForeignKey(Estudante, on_delete=models.RESTRICT, blank=True, null=True)
    local_do_estagio_de_pretensao = models.ForeignKey(Locais_de_Estagio, related_name='pretensao', on_delete=models.RESTRICT, blank=True, null=True)
    local_do_estagio = models.ForeignKey(Locais_de_Estagio, on_delete=models.RESTRICT, blank=True, null=True)
    data_inicio = models.DateField(verbose_name= "Data inicio", blank=True, null=True)
    data_fim = models.DateField(verbose_name="Data termino", blank=True, null=True)
    TCE = models.FileField(upload_to='TCE', verbose_name='Termo de Compromisso de Estágio', null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.estudante.pessoa.nome
    
class Processo(models.Model):

    n_processo = models.CharField(max_length=8, verbose_name='Número do processo', null=True)  
    estudante_vaga = models.ForeignKey(Estudante_Vaga, on_delete=models.CASCADE)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    
@receiver(post_save, sender=Processo)
def generate_process_number(sender, instance, created, **kwargs):
    if created and not instance.n_processo:  # Verifica se o objeto foi criado recentemente e se o número do processo já existe
        random_part = ''.join(random.choices(string.digits, k=5))
        print('ID:', instance.id)
        n_processo='{}{}'.format(random_part, instance.id)
        aux=len(n_processo)
        if aux>8:
            while aux>8:
                n_processo = n_processo[1:]
                aux=len(n_processo)
                print(n_processo)
        instance.n_processo='{:8}'.format(n_processo.zfill(8))
        instance.save()

class Historico_Processo(models.Model):
    STATUS_CHOICES = (
        ('0', 'Aguardando liberação de vaga'),
        ('1', 'Lista de espera'),
        ('2', 'Aguardando reenvio do TCE'),
        ('3', 'Aguardando termo assinado pelas partes'),
        ('4', 'Processo de seleção concluída'),
        ('5', 'Estágio concluído'),
        ('6', 'Candidatura cancelada')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status', default=0)
    processo=models.ForeignKey(Processo, on_delete=models.CASCADE, null=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False)
    mensagem=models.TextField(blank=True)
