from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from autenticacao.models import Pessoa
from django.db.models import Count
from django.db.models.functions import Extract
import uuid
from django.utils import timezone

class Bairro(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Bairro')


class Logradouro(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Logradouro')


class Endereco(models.Model):
    referencia = models.CharField(
        max_length=200, verbose_name='Referência', blank=True)
    bairro = models.ForeignKey(
        Bairro, verbose_name='Bairro', on_delete=models.PROTECT)
    logradouro = models.ForeignKey(
        Logradouro, verbose_name='Logradouro', on_delete=models.PROTECT)

class Tipo_OS(models.Model):
    
    nome=models.CharField(max_length=100, verbose_name='Tipo de OS', blank=True)
    sigla=models.CharField(max_length=10, verbose_name='Sigla', blank=True, null=True)
    def __str__(self):
        return self.nome

class Sub_Tipo_OS(models.Model):
    
    tipo_os=models.ForeignKey(Tipo_OS, on_delete=models.CASCADE)
    nome=models.CharField(max_length=100, verbose_name='Sistema', blank=True)
    sigla=models.CharField(max_length=10, verbose_name='Sigla', blank=True, null=True)
    def __str__(self):
        return self.nome
    
class Funcionario_DEV_OS(models.Model):
    def __str__(self):
        return self.pessoa.nome
    NIVEL_CHOICES=(
        ('0','0 - Agente de atendimento'),
        ('1','1 - Suporte de campo'),
        ('2','2 - Suporte avançado'),
        ('3','3 - Coordenador de serviços públicos'),
    )

    pessoa = models.ForeignKey(Pessoa, models.CASCADE)
    tipo_os =  models.ManyToManyField(Tipo_OS)
    nivel = models.CharField(max_length=1, verbose_name='Nível de acesso', choices=NIVEL_CHOICES, null=True, default='0')
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')


class TotalOSPorSemanaAno(models.Model):
    ano = models.IntegerField()
    semana = models.IntegerField()
    total_os = models.IntegerField()


class TotalOSPorMesAno(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()
    total_os = models.IntegerField()

class DevOrdemDeServico(models.Model):
    STATUS_CHOICES=(
        ('0','Novo'),
        ('1','Aguardando'),
        ('2','Em execução'),
        ('f','Finalizado')
    )
    PRIORIDADE_CHOICES=(
        ('0','Normal'),
        ('1','Moderada'),
        ('2','Urgente'),
    )

    
    tipo=models.ForeignKey(Tipo_OS, on_delete=models.PROTECT, null=True)
    numero = models.CharField(max_length=130, verbose_name='Nº da OS', blank=True)
    prioridade =models.CharField(max_length=1, verbose_name='Prioridade', default='0', choices=PRIORIDADE_CHOICES, null=True)

    dt_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de solicitação', blank=True)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    # logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    # bairro = models.CharField(max_length=150, verbose_name='Bairro')
    # referencia = models.CharField(max_length=200, verbose_name='Referência', blank=True)

    nome_do_contribuinte = models.CharField(max_length=200, verbose_name='Nome do contribuinte', blank=True)
    telefone_do_contribuinte = models.CharField(max_length=12, verbose_name='Telefone do contribuinte', blank=True)
    secretaria_solicitante = models.CharField(max_length=200, verbose_name='Secretária solicitante', blank=True)

    cadastrado_por = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)   

    motivo_reclamacao = models.TextField(verbose_name='Motivo da solicitação')            
    
    status =models.CharField(max_length=1, verbose_name='Status', choices=STATUS_CHOICES, null=True, default='0')
    pontos_atendidos=models.PositiveIntegerField(default=0)
    dt_conclusao = models.DateTimeField(verbose_name='Data de conclusão', blank=True, null=True)

    def semana_atendimento(self):
        return self.dt_conclusao.isocalendar()[1]

    @staticmethod
    def total_os_por_semana_ano():
        # Obtém a contagem de OS por semana e ano
        os_por_semana_ano = DevOrdemDeServico.objects.filter(status='f').annotate(ano=Extract('dt_conclusao', 'year'), semana=Extract('dt_conclusao', 'week')).values('ano', 'semana').annotate(total_os=Count('id'))

        # print(os_por_semana_ano)
        # Salva os valores na tabela TotalOSPorSemanaAno
        for item in os_por_semana_ano:
            ano = item['ano']
            semana = item['semana']
            total_os = item['total_os']
            # print(semana, ano, total_os)
            TotalOSPorSemanaAno.objects.create(ano=ano, semana=semana, total_os=total_os)
    
    @staticmethod
    def total_os_por_mes_ano():
        # Obtém a contagem de OS por mês
        os_por_mes = DevOrdemDeServico.objects.filter(status='f').annotate(ano=Extract('dt_conclusao', 'year'), mes=Extract('dt_conclusao', 'month')).values('ano', 'mes').annotate(total=Count('id'))

        # Salva os valores na tabela TotalOSPorMes
        for item in os_por_mes:            
            ano = item['ano']
            mes = item['mes']
            total_os = item['total']
            print(mes, ano, total_os)
            TotalOSPorMesAno.objects.create(ano=ano, mes=mes, total_os=total_os)


    class Meta:
        ordering = ['-dt_solicitacao']

    def gerar_protocolo(self):        
        self.numero = f"{self.tipo.sigla}{int(uuid.uuid4().hex[:10], 16)}/{self.dt_solicitacao.strftime('%y')}"
        self.save()
        return self.numero
    
    def finalizar_chamado(self):
        
        if self.status == 'f':
            return "Chamado já foi finalizado."
            
        self.status = 'f'
        self.dt_conclusao = timezone.now()
        self.save()
        return "Chamado finalizado com sucesso."

class OS_ext(models.Model):    
    os=models.ForeignKey(DevOrdemDeServico, on_delete=models.PROTECT)
    equipe=models.ManyToManyField(Funcionario_DEV_OS, blank=True, null=True)
    cod_veiculo=models.CharField(max_length=14, verbose_name='Código do veículo', blank=True)

class DEV_OS_Linha_Tempo(models.Model):
    os=models.ForeignKey(DevOrdemDeServico, on_delete=models.CASCADE)
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    mensagem=models.TextField()
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data da mensagem', blank=True)
