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
    ramo=models.CharField(max_length=64, verbose_name='Ramo de atuação')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    
    __str__ = lambda self: self.ramo
    
class Empresa(models.Model):
    cnpj=models.CharField(max_length=18, verbose_name='CNPJ', unique=True)
    nome=models.CharField(max_length=128, verbose_name='Nome da empresa')
    porte=models.ForeignKey(Porte_da_Empresa, on_delete=models.CASCADE, verbose_name='Porte da empresa')
    atividade=models.ManyToManyField(Atividade, verbose_name='Atividade')
    ramo=models.ManyToManyField(Ramo_de_Atuacao, verbose_name='Ramo de atuação')
    outro_ramo=models.CharField(max_length=64, verbose_name='Outro ramo', blank=True, null=True)
    receber_noticias=models.BooleanField(default=False, verbose_name='Deseja receber notificações sobre compras da prefeitura?')
    telefone=models.CharField(max_length=15, verbose_name='Telefone de contato', null=True, blank=True)
    whatsapp=models.CharField(max_length=15, verbose_name='Whatsapp da empresa', null=True, blank=True)
    email=models.EmailField(verbose_name='E-mail da empresa', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição da empresa')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    validacao=models.BooleanField(default=False, verbose_name='Validação da empresa')
    cadastrada_na_vitrine=models.BooleanField(default=False, verbose_name='Cadastrado na Vitrine Virtual?')
    cadastrada_como_fornecedor=models.BooleanField(default=False, verbose_name='Cadastrado como fornecedor da prefeitura?')
    
class Produto(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    nome=models.CharField(max_length=128, verbose_name='Nome do produto')
    descricao=models.TextField(verbose_name='Descrição do produto')
    preco=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    imagem=models.ImageField(upload_to='produtos/', verbose_name='Imagem do produto')
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
    
class Registro_no_vitrine_virtual(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    produtos=models.ManyToManyField(Produto, verbose_name='Produtos')
    dt_register=models.DateField(auto_now_add=True, verbose_name='Data de cadastro')
    user_register=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que cadastrou', null=True)
