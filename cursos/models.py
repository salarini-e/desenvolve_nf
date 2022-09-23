from django.db import models
from django.contrib.auth.models import User

class Instituicao(models.Model):

    nome = models.CharField(max_length=150)

    def __str__(self):
            return '%s' % (self.nome)

class Local(models.Model):

    nome = models.CharField(max_length=150, verbose_name='Nome do local')
    endereco = models.CharField(max_length=150, verbose_name='Endereço')
    bairro = models.CharField(max_length=80, verbose_name='Bairro')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
            return '%s' % (self.nome)

class Categoria(models.Model):
    
    nome = models.CharField(max_length=150, verbose_name='Nome da categoria')

    def __str__(self):
            return '%s' % (self.nome)

class Curso(models.Model):

    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)    
    carga_horaria = models.CharField(max_length=150)    
    descricao = models.TextField(default='')
    ativo=models.BooleanField(default=True)

    dt_inclusao=models.DateField(auto_now_add=True, editable=False)
    dt_alteracao=models.DateField(auto_now=True)
    user_inclusao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userInclusao')
    user_ultima_alteracao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userAlteracao', null=True, blank=True)

    def __str__(self):
            return '%s' % (self.nome)

class Professor(models.Model):
    
    nome = models.CharField(max_length=150, verbose_name='Nome completo do professor')
    celular = models.CharField(max_length=15, verbose_name='Celular')
    email = models.EmailField(verbose_name='Email', blank=True)  
    endereco = models.CharField(max_length=150, blank=True, null=True, verbose_name='Endereço')
    bairro = models.CharField(max_length=80, blank=True, null=True)
    cpf = models.CharField(max_length=14, verbose_name='CPF')            
    dt_inclusao=models.DateField(auto_now_add=True)  

    def __str__(self):
            return '%s' % (self.nome)

class Turma(models.Model):
    
    STATUS_CHOICES=(
                            ('pre', 'Pré-inscrição'),
                            ('agu', 'Aguardando'),
                            ('ati', 'Ativa'),
                            ('acc', 'Ativa e aceitando candidatos'),
                            ('enc', 'Encerrada'),
    )
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Atividade')
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    horario = models.CharField(max_length=150)
    instrutor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    qnt=models.IntegerField(verbose_name='Quantidade de alunos permitidos')
    idade_min = models.IntegerField(verbose_name='Idade mínima', null=True, blank=True)
    idade_max = models.IntegerField(verbose_name='Idade máxima', null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()    
    
    dt_inclusao=models.DateField(auto_now_add=True, editable=False)
    dt_alteracao=models.DateField(auto_now=True)
    user_inclusao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='TurmaUserInclusao')
    user_ultima_alteracao=models.ForeignKey(User, on_delete=models.CASCADE, related_name='TurmaUserAlteracao', null=True, blank=True)
    status=models.CharField(max_length=3, default='pre', choices=STATUS_CHOICES, verbose_name='Qual o status da turma?')
    def __str__(self):
            return '%s %s - %s - %s' % (self.curso.nome, self.id, self.local, self.horario)

class Candidato(models.Model):
    
    SEXO_CHOICES=(
                            ('M', 'Masculino'),
                            ('F', 'Feminino'),                                                      
    )

    ESCOLARIDADE_CHOICES=(
                            ('efi', 'Ensino Fundamental Incompleto'),
                            ('efc', 'Ensino Fundamental Completo'),
                            ('emi', 'Ensino Médio Incompleto'),                            
                            ('emc', 'Ensino Médio Completo'),                            
                            ('ct', 'Curso Técnico'),
                            ('esi', 'Ensino Superior Incompleto'),
                            ('esc', 'Ensino Superior Completo'),                            
    )
    
    ESTADOCIVIL_CHOICES=(
                            ('s', 'Solteiro(a)'),
                            ('c', 'Casado(a)'),
                            ('s', 'Separado(a)'),
                            ('d', 'Divorciado(a)'),
                            ('v', 'Viúvo(a)'),                            
    )


    nome = models.CharField(max_length=150, verbose_name='Nome completo do candidato')
    celular = models.CharField(max_length=15, verbose_name='Celular p/ contato do candidato') 
    email = models.EmailField(verbose_name='Email p/ contato do candidato')    
    dt_nascimento = models.DateField(verbose_name='Data de Nascimento')    
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Qual foi o sexo atribuído no seu nascimento?')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    endereco = models.CharField(max_length=150, null=True, verbose_name='Endereço do candidato')
    # estado
    # cidade    
    bairro = models.CharField(max_length=80, null=True)
    cpf = models.CharField(max_length=150, verbose_name='CPF')      
    rg = models.CharField(max_length=12, verbose_name='RG', blank=True)
    profissão = models.CharField(max_length=150, verbose_name='Profissão')        
    escolaridade = models.CharField(max_length=3, choices=ESCOLARIDADE_CHOICES, verbose_name='Escolaridade')        
    nome_da_mãe = models.CharField(max_length=150, verbose_name='Nome completo da mãe do candidato')
    estado_civil = models.CharField(max_length=1, choices=ESTADOCIVIL_CHOICES, verbose_name='Estado Civil')        
    aceita_mais_informacoes = models.BooleanField(verbose_name='Declaro que aceito receber email com as informações das atividades')    
    li_e_aceito_termos = models.BooleanField(default=False, verbose_name='Li e aceito os termos')    
    turmas = models.ManyToManyField(Turma)
    turmas_selecionado = models.ManyToManyField(Turma, related_name='tselecionado', null=True, blank=True)    
    dt_inclusao=models.DateField(auto_now_add=True)

    def __str__(self):
            return '%s' % (self.nome)

# class Selecionado(models.Model):

#     candidato=models.ForeignKey(Candidato, on_delete=models.CASCADE)

#     def __str__(self):
#             return '%s' % (self.candidato.nome)

class Aluno(models.Model):
    
    SEXO_CHOICES=(
                            ('M', 'Masculino'),
                            ('F', 'Feminino'),                                                      
    )

    nome = models.CharField(max_length=150, verbose_name='Nome completo do aluno')
    celular = models.CharField(max_length=15, verbose_name='Celular p/ contato do aluno')
    email = models.EmailField(verbose_name='Email p/ contato do aluno')    
    dt_nascimento = models.DateField(verbose_name='Data de Nascimento do aluno')    
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Qual foi o sexo atribuído no nascimento?')
    endereco = models.CharField(max_length=150, null=True, verbose_name='Endereço do aluno')
    bairro = models.CharField(max_length=80, null=True)
    cpf = models.CharField(max_length=150, verbose_name='CPF')            
    dt_inclusao=models.DateField(auto_now_add=True)

    def __str__(self):
            return '%s' % (self.nome)

class Matricula(models.Model):

    turma =  models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
            return '%s' % (self.aluno.nome)