from django.db import models
from django.contrib.auth.models import User

class Instituicao(models.Model):

    nome = models.CharField(max_length=150)

    def __str__(self):
            return '%s' % (self.nome)

class Local(models.Model):

    nome = models.CharField(max_length=150)

    def __str__(self):
            return '%s' % (self.nome)

class Categoria(models.Model):
    
    nome = models.CharField(max_length=150)

    def __str__(self):
            return '%s' % (self.nome)

class Curso(models.Model):

    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    carga_horaria = models.CharField(max_length=150)    
    descricao = models.TextField(default='')
    ativo=models.BooleanField(default=True)

    dt_inclusao=models.DateField(auto_now_add=True, editable=False)
    dt_alteracao=models.DateField(auto_now=True)
    user_inclusao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userInclusao')
    user_ultima_alteracao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userAlteracao')

    def __str__(self):
            return '%s' % (self.nome)

class Candidato(models.Model):
    
    SEXO_CHOICES=(
                            ('M', 'Masculino'),
                            ('F', 'Feminino'),                                                      
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)    
    dt_nascimento = models.DateField(verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Qual foi o sexo atribuído no seu nascimento?')
    email = models.EmailField()
    celular = models.CharField(max_length=12)
    
    def __str__(self):
            return '%s' % (self.nome)

class Selecionado(models.Model):

    candidato=models.ForeignKey(Candidato, on_delete=models.CASCADE)

    def __str__(self):
            return '%s' % (self.nome)

class Aluno(models.Model):

    selecionado=models.ForeignKey(Selecionado, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=150)    

    def __str__(self):
            return '%s' % (self.nome)

class Turma(models.Model):
    
    # instrutor = 
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    horario=models.CharField(max_length=150)
    data_inicio=models.DateField()
    data_final=models.DateField()    

    def __str__(self):
            return '%s %s' % (self.curso.nome, self.data_inicio)

class Matricula(models.Model):

    turma =  models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_matricula = models.DateField()

    def __str__(self):
            return '%s' % (self.nome)