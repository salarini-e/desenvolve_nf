from django.db import models
from django.core.exceptions import ValidationError
from autenticacao.functions import validate_cpf

class PessoaRecadastramento(models.Model):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    responsavel_tributario = models.CharField(max_length=150, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    nome_do_contribuinte = models.CharField(max_length=150)
    celular = models.CharField(max_length=15, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    rua = models.CharField(max_length=150, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

    def check_cpf_or_cnpj(self):
        if not self.cpf and not self.cnpj:
            raise ValidationError("Pelo menos um dos campos CPF ou CNPJ deve ser preenchido.")
        self.cpf = validate_cpf(self.cpf) if self.cpf else self.cpf

    def change_all_to_lower_case(self):
        
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
    requerente = models.ForeignKey(PessoaRecadastramento, on_delete=models.CASCADE, null=True, blank=True)
    requerimento = models.CharField(max_length=20)
    ano = models.IntegerField()    
    localizacao = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        existing_process = Processo.objects.filter(requerimento=self.requerimento, ano=self.ano).exists()
        if existing_process:
            raise ValidationError({"requerimento": ["Já existe um processo com o mesmo requerimento e ano."]})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.requerimento

class Inscricao(models.Model):
    pessoa_recadastramento = models.ForeignKey(PessoaRecadastramento, on_delete=models.CASCADE)
    numero_inscricao = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.numero_inscricao