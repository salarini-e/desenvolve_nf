from django.db import models

class Universidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome_universidade")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome_curso")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    curso_id_universidade = models.ForeignKey(Universidade, on_delete= models.CASCADE)
   
    def __str__(self):
        return self.nome
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome_secretaria")
    local = models.CharField(max_length=200, verbose_name="local_secretaria")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    
    def __str__(self):
        return self.nome

class Vagas(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome_vagas")
    quantidade_de_vagas = models.IntegerField(verbose_name="quantidade_de_vagas")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    vagas_id_secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    vagas_id_curso = models.ManyToManyField(Curso)
    
class Supervisor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome_supervisor")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    supervisor_id_secretaria = models.ForeignKey(Secretaria, on_delete= models.CASCADE)
    supervisor_id_vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Aluno(models.Model):
    STATUS_CHOICES = (
        ('0', 'Candidato'),
        ('1', 'Estágiario'),
    )
    nome = models.CharField(max_length=200, verbose_name= "nome_aluno")
    contato = models.IntegerField(verbose_name= "contato_aluno")
    matricula = models.IntegerField(verbose_name= "matricula")
    data_inclusao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    data_incio = models.DateField(verbose_name= "data_inicio", blank=True, null=True)
    data_fim = models.DateField(verbose_name="data_termino", blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='Status', default=0)
    aluno_id_curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=True, null=True)
    aluno_id_supervisor = models.ForeignKey(Supervisor, on_delete=models.RESTRICT, blank=True, null=True)
    def __str__(self):
        return self.nome