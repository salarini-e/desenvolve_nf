from django.db import models

class Universidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome_universidade")
    
    def __str__(self):
        return self.name

class Curso(models.Model):
    nome = models.CharField(max_length=50, verbose_name="nome_curso")
    curso_id_universidade = models.ForeignKey(Universidade, on_delete= models.RESTRICT)
   
    def __str__(self):
        return self.name
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome_secretaria")
    local = models.CharField(max_length=200, verbose_name="local_secretaria")
    
    def __str__(self):
        return self.name
    
class Supervisor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome_supervisor")
    supervisor_id_secretaria = models.ForeignKey(Secretaria, on_delete= models.CASCADE)
   
    def __str__(self):
        return self.name

class Aluno(models.Model):
    nome = models.CharField(max_length=200, verbose_name= "nome_aluno")
    contato = models.IntegerField(verbose_name= "contato_aluno")
    matricula = models.IntegerField(verbose_name= "matricula")
    data_incio = models.DateField(verbose_name= "data_inicio")
    data_fim = models.DateField(verbose_name="data_termino")
    aluno_id_curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    aluno_id_supervisor = models.ForeignKey(Supervisor, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
