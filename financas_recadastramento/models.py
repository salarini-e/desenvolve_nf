from django.db import models
from django.core.exceptions import ValidationError

class PessoaRecadastramento(models.Model):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    responsavel_tributario = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    nome_do_contribuinte = models.CharField(max_length=150)
    celular = models.CharField(max_length=15, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    rua = models.CharField(max_length=150, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    email = models.EmailField(blank=True)

    def check_cpf_or_cnpj(self):
        if not self.cpf and not self.cnpj:
            raise ValidationError("Pelo menos um dos campos CPF ou CNPJ deve ser preenchido.")

    def change_all_to_lower_case(self):
        self.responsavel_tributario = self.responsavel_tributario.lower()
        self.nome_do_contribuinte = self.nome_do_contribuinte.lower()
        self.rua = self.rua.lower()
        self.complemento = self.complemento.lower() if self.complemento else self.complemento
        self.bairro = self.bairro.lower()
        self.cidade = self.cidade.lower()
        self.estado = self.estado.lower()
        self.email = self.email.lower()

    def save(self, *args, **kwargs):
        self.check_cpf_or_cnpj()
        self.change_all_to_lower_case()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_do_contribuinte

class Processo(models.Model):
    pessoa_recadastramento = models.ForeignKey(PessoaRecadastramento, on_delete=models.CASCADE, null=True, blank=True)
    requerente = models.CharField(max_length=150)
    requerimento = models.CharField(max_length=20)
    ano = models.IntegerField()    
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.numero

class Inscricao(models.Model):
    pessoa_recadastramento = models.ForeignKey(PessoaRecadastramento, on_delete=models.CASCADE)
    numero_inscricao = models.CharField(max_length=20)

    def __str__(self):
        return self.numero