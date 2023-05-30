from django.db import models
from autenticacao.models import Pessoa

class Universidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome universidade")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome curso")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    universidade = models.ForeignKey(Universidade, on_delete= models.CASCADE)
   
    def __str__(self):
        return self.nome
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome secretaria")
    local = models.CharField(max_length=200, verbose_name="Local Secretaria")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    
    def __str__(self):
        return self.nome

class Vagas(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome vagas")
    quantidade_de_vagas = models.IntegerField(verbose_name="Quantidade de vagas")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    img = models.ImageField(upload_to = 'estagio/media/banner_vagas/', null=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    curso = models.ManyToManyField(Curso)
    
    def __str__(self):
        return self.nome
    
class Supervisor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome supervisor")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    secretaria = models.ForeignKey(Secretaria, on_delete= models.CASCADE)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Estudante(models.Model):
    STATUS_CHOICES = (
        ('0', 'Candidato'),
        ('1', 'Estágiario'),
    )
    pessoa = models.ForeignKey(Pessoa, related_name='aluno_pessoa', on_delete=models.PROTECT)
    matricula = models.CharField(max_length=50, verbose_name= "Matricula")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    universidade = models.ForeignKey(Universidade, on_delete=models.RESTRICT)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=True, null=True)
    
    def __str__(self):
        return self.pessoa.nome
    
class Estudante_Vaga(models.Model):
    STATUS_CHOICES = (
        ('0', 'Candidato'),
        ('1', 'Estágiario'),
        ('2', 'Concluido')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status', default=0)
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_fim = models.DateField(verbose_name="Data termino", blank=True, null=True)
    data_inicio = models.DateField(verbose_name= "Data inicio", blank=True, null=True)
    vaga = models.ForeignKey(Vagas, on_delete=models.RESTRICT)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.RESTRICT, blank=True, null=True)
    estudante = models.ForeignKey(Estudante, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return self.estudante.pessoa.nome