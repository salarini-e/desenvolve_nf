from django.db import models
from django.contrib.auth.models import User

class Conselheiros(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)    
    cpf = models.CharField(max_length=11, verbose_name='CPF')    
    ativo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.nome

class Data_Reunião(models.Model):
    DIA_CHOICES = [
        ('S', 'Segunda-feira'),
        ('T', 'Terça-feira'),
        ('Q', 'Quarta-feira'),
        ('Q', 'Quinta-feira'),
        ('S', 'Sexta-feira'),
        ('S', 'Sábado'),
        ('D', 'Domingo'),
    ]
    data = models.DateField()
    dia = models.CharField(max_length=1, choices=DIA_CHOICES, verbose_name='Dia da semana')

    def __str__(self):
        return f'{self.data}'

class Pauta_de_Julgamento(models.Model):
    
    representante = models.CharField(max_length=150)
    relator = models.CharField(max_length=150)
    data = models.DateField()    
    hora = models.TimeField()    
    local = models.CharField(max_length=100)
    processos = models.TextField(verbose_name='Processos em pauta (Separe por ponto e vírgula)')

    numero = models.IntegerField()    
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField()

    def __str__(self):
        return f'{self.numero}/{self.data.year}'
    
class Sumulas(models.Model):
    data = models.DateField()
    numero = models.CharField(max_length=50)
    assunto = models.CharField(max_length=100)
    conteudo = models.TextField(verbose_name='Texto da Súmula')

    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField()

    def __str__(self):
        return f'{self.numero}/{self.data.year} - {self.assunto}'


class Acordao(models.Model):
    reuniao = models.ForeignKey(Pauta_de_Julgamento, on_delete=models.CASCADE)
    data = models.DateField()
    numero = models.CharField(max_length=50, verbose_name='Número do Acórdão')
    processo = models.CharField(max_length=50, verbose_name='Número do processo')
    recorrente = models.CharField(max_length=150)    
    recorrido = models.CharField(max_length=150)    
    relator = models.CharField(max_length=150)    
    ementa = models.TextField(verbose_name='Ementa do Acórdão')
    inteiro = models.FileField(upload_to='acordaos/', verbose_name='Arquivo do Acórdão')
    
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField()

    def __str__(self):
        return f'{self.numero}/{self.data.year} - {self.recorrente}'

class Ata(models.Model):
    reuniao = models.ForeignKey(Pauta_de_Julgamento, on_delete=models.CASCADE, verbose_name='Reunião')
    data = models.DateField()
    numero = models.CharField(max_length=50)
    ata = models.FileField(upload_to='atas/', verbose_name='Arquivo da Ata', null=True)
    participantes = models.ManyToManyField(Conselheiros)
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField()

    def __str__(self):
        return f'{self.numero}/{self.reuniao.numero}/{self.data.year}'
    
class Voto_Relator(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='votos/', verbose_name='Arquivo do Voto')
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
#formularios e declarações
class Classe_Formulario(models.Model):
    nome = models.CharField(max_length=100)
    div_id = models.CharField(max_length=10)
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    def get_formularios(self):
        return Formularios.objects.filter(classe=self)
    
class Formularios(models.Model):
    classe = models.ForeignKey(Classe_Formulario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='formularios/', verbose_name='Arquivo do Formulário')
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} - {self.classe.nome}'