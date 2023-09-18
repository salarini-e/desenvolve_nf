from django.db import models
from django.contrib.auth.models import User


class Porte_da_Empresa(models.Model):
    porte=models.CharField(max_length=32, verbose_name='Porte da empresa')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')

    __str__ = lambda self: self.porte

class Atividade(models.Model):
    atividade=models.CharField(max_length=64, verbose_name='Atividade')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')

    __str__ = lambda self: self.atividade
    
class Ramo_de_Atuacao(models.Model):
    ramo=models.CharField(max_length=164, verbose_name='Ramo de atuação')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    
    __str__ = lambda self: self.ramo
    
class Empresa(models.Model):
    cnpj=models.CharField(max_length=18, verbose_name='CNPJ', unique=True)
    nome=models.CharField(max_length=128, verbose_name='Nome da empresa')
    porte=models.ForeignKey(Porte_da_Empresa, on_delete=models.CASCADE, verbose_name='Porte da empresa')
    atividade=models.ManyToManyField(Atividade, verbose_name='Atividade')
    outra_atividade=models.CharField(max_length=64, verbose_name='Outra atividade', blank=True, null=True)
    ramo=models.ManyToManyField(Ramo_de_Atuacao, verbose_name='Ramo de atuação')
    outro_ramo=models.CharField(max_length=64, verbose_name='Outro ramo', blank=True, null=True)
    receber_noticias=models.BooleanField(default=False, verbose_name='Deseja receber notificações sobre compras da prefeitura?')
    telefone=models.CharField(max_length=15, verbose_name='Telefone de contato', null=True, blank=True)
    whatsapp=models.CharField(max_length=15, verbose_name='Whatsapp da empresa', null=True, blank=True)
    email=models.EmailField(verbose_name='E-mail da empresa', null=True, blank=True)
    site=models.URLField(verbose_name='Site da empresa', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição da empresa')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    validacao=models.BooleanField(default=False, verbose_name='Validação da empresa')
    cadastrada_na_vitrine=models.BooleanField(default=False, verbose_name='Cadastrado na Vitrine Virtual?')
    cadastrada_como_fornecedor=models.BooleanField(default=False, verbose_name='Cadastrado como fornecedor da prefeitura?')
    
class Registro_no_vitrine_virtual(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    logo=models.ImageField(upload_to='logos/', verbose_name='Logo da empresa', null=True, blank=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)

class Produto(models.Model):
    rg_vitrine=models.ForeignKey(Registro_no_vitrine_virtual, on_delete=models.CASCADE, verbose_name='Registro da vitrine virtual')
    nome=models.CharField(max_length=128, verbose_name='Nome do produto ou serviço')
    descricao=models.TextField(verbose_name='Descrição do produto')
    imagem=models.ImageField(upload_to='produtos/', verbose_name='Imagem do produto')
    validacao_da_equipe=models.BooleanField(default=False, verbose_name='Validação da Sala do Empreendedor')
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)

class Trabalho_Faccao(models.Model):
    nome = models.CharField(max_length=128, verbose_name='Nome do trabalho')
    def __str__(self) -> str:
        return self.nome
class Equipamentos_Faccao(models.Model):
    nome = models.CharField(max_length=128, verbose_name='Nome do equipamento')
    def __str__(self) -> str:
        return self.nome
    
class Tipo_produto_faccao(models.Model):
    nome = models.CharField(max_length=128, verbose_name='Nome do produto')
    def __str__(self) -> str:
        return self.nome
    
class Faccao_legal(models.Model):
    
    TEMPO_CHOICES=(
        ('0','Menos de 1 ano'),
        ('1','De 1 a 3 anos'),
        ('2','Mais de 3 anos'),
    )
    AREA_CHOICES=(
        ('s', 'Sim'),
        ('n', 'Não'),
    )
    TAMANHO_AREA_CHOICES=(
        ('0', 'Menos de 6m²'),
        ('1', 'De 6 a 16m²'),
        ('2', 'De 16 a 50m²'),
        ('3', 'Mais de 50m²'),
    )
    QNT_COLABORADORES_CHOICES=(
        ('0', '1 a 2'),
        ('1', '3 a 4'),
        ('2', '5 a 10'),
        ('3', 'Mais de 10'),
    )
    SITUACAO_CHOICES=(
        ('p', 'Pouco'),
        ('s', 'Suficiente'),
        ('d', 'Em demasia'),    
    )
    REMUNERACAO_CHOICES=(
        ('bx', 'Baixa'),
        ('rg', 'Regular'),
        ('bo', 'Boa'),
        ('ot', 'Ótima')   
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário', null=True)
    possui_mei=models.BooleanField(default=False, verbose_name='Possui MEI ou empresa de outro porte?')
    cnpj=models.CharField(max_length=18, verbose_name='CNPJ', null=True, blank=True)
    tempo_que_trabalha=models.CharField(max_length=1, verbose_name='Trabalha com facção há quanto tempo', choices=TEMPO_CHOICES)
    trabalha_com = models.ManyToManyField(Trabalho_Faccao, verbose_name='Trabalha com:', null=True)
    equipamentos = models.ManyToManyField(Equipamentos_Faccao, verbose_name='Quais equipamentos possui?')
    area = models.CharField(max_length=1, verbose_name='Possui área de trabalho separada da residência?', choices=AREA_CHOICES)
    tamanho_area = models.CharField(max_length=1, verbose_name='Qual o tamanho da área de trabalho?', choices=TAMANHO_AREA_CHOICES)
    possui_colaboradores = models.BooleanField(default=False, verbose_name='Possui colaboradores?')
    qtd_colaboradores = models.IntegerField(verbose_name='Quantos colaboradores possui?', null=True, blank=True)
    tipo_produto = models.ManyToManyField(Tipo_produto_faccao, verbose_name='Que tipos de produtos produz?')
    outro_produto = models.CharField(max_length=128, verbose_name='Outro produto, descreva', null=True, blank=True)
    situacao_trabalho = models.CharField(max_length=1, verbose_name='Geralmente, como está de trabalho?', choices=SITUACAO_CHOICES)
    situacao_remuneracao = models.CharField(max_length=2, verbose_name='Como está a remuneração?', choices=REMUNERACAO_CHOICES)
    qual_seu_sonho_no_setor = models.TextField(verbose_name='Qual seu sonho no setor?', null=True, blank=True)