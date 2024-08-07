from django.db import models
from sala_do_empreendedor.models import Processo_Digital, Profissao
from django.utils import timezone
from sala_do_empreendedor.models import Agente_Sanitario
from PIL import Image
from django.core.exceptions import ValidationError
from sala_do_empreendedor.models import Agente_Tributario, Agente_Ambiental, Agente_Sanitario, Agente
import re
from django.utils.html import format_html

DOC_STATUS_CHOICES=(
        ('0', 'Aguardando avaliação'),
        ('1', 'Aprovado'),
        ('2', 'Aguardando reenvio!'),
        # ('3', 'Atualização requerida'),
    )

class LimitedImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.allowed_formats = kwargs.pop('allowed_formats', ['jpeg', 'png'])
        self.max_size = kwargs.pop('max_size', None)
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value:
            image = Image.open(value)
            format = image.format.lower()
            if format not in self.allowed_formats:
                raise ValidationError(f'A imagem deve estar nos formatos {", ".join(self.allowed_formats)}.')

            if image.size[0] > self.max_size[0] or image.size[1] > self.max_size[1]:
                raise ValidationError(f'A imagem não pode ser maior que {self.max_size[0]}x{self.max_size[1]} pixels.')


# Create your models here.
class RequerimentoISS(models.Model):
    
    AUTONOMO_LOCALIZADO_CHOICES=(
        ('s', 'Sim'),
        ('n', 'Não'),   
    )
    
    processo = models.ForeignKey(Processo_Digital, on_delete=models.CASCADE, verbose_name='Processo', null=True)     
    profissao = models.ForeignKey(Profissao, on_delete=models.CASCADE, verbose_name='Profissão')
    autonomo_localizado = models.CharField(max_length=1, verbose_name='Autônomo localizado?', choices=AUTONOMO_LOCALIZADO_CHOICES)    
    n_inscricao = models.CharField(max_length=128, verbose_name='Número de inscrição', null=True, blank=True)
    dt_solicitacao = models.DateField(auto_now_add=True, verbose_name='Data de solicitação', null=True)
    dt_atualizacao = models.DateField(auto_now=True, verbose_name='Data de atualização', null=True)
    
    def save(self, *args, **kwargs):
        self.dt_atualizacao = timezone.now()
        super(RequerimentoISS, self).save(*args, **kwargs)

    def exist_boleto_requerimento(self):
        boleto = BoletosRequerimentoISS.objects.filter(requerimento=self)
        return boleto.exists() and boleto.first().boleto_requerimento
    
    def boleto_sanitario_gerado(self):
        boleto = BoletosRequerimentoISS.objects.filter(requerimento=self)
        return boleto.exists() and boleto.first().boleto_licenca_sanitaria
    
    def sanitaria_comprovante_em_analise(self):
        boleto = BoletosRequerimentoISS.objects.filter(requerimento=self)
        return boleto.exists() and boleto.first().comprovante_licenca_sanitaria
    
    def exist_licenca_sanitaria(self):
        doc = DocumentosLicencaSanitaria.objects.filter(requerimento=self)
        return doc.exists() and doc.first().licenca_sanitaria
    
    def get_url_licenca_sanitaria(self):
        doc = DocumentosLicencaSanitaria.objects.filter(requerimento=self)
        return doc.first().licenca_sanitaria.url
    
    def exist_licenca_ambiental(self):
        doc = DocumentosLicencaAmbiental.objects.filter(requerimento=self)
        return doc.exists() and doc.first().licenca_ambiental
    
    def get_url_licenca_ambiental(self):
        doc = DocumentosLicencaAmbiental.objects.filter(requerimento=self)
        return doc.first().licenca_ambiental.url
    
    def ambiental_comprovante_em_analise(self):
        boleto = BoletosRequerimentoISS.objects.filter(requerimento=self)
        return boleto.exists() and boleto.first().comprovante_licenca_ambiental

    def boleto_ambiental_gerado(self):
        boleto = BoletosRequerimentoISS.objects.filter(requerimento=self)
        return boleto.exists() and boleto.first().boleto_licenca_ambiental
    
class DocumentosRequerimentoISS(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)

    rg = models.FileField(upload_to='processos/rg_cnh/', verbose_name='RG/CNH/Passaporte', null=True)
    comprovante_endereco = models.FileField(upload_to='processos/comprovante_endereco/', verbose_name='Comprovante de endereço', null=True)
    diploma_ou_certificado = models.FileField(upload_to='processos/diploma_ou_certificado/', verbose_name='Diploma ou certificado', null=True, blank=True)
    
    #Comum com Meio Ambiente
    espelho_iptu = models.FileField(upload_to='processos/espelho_iptu/', verbose_name='Espelho do IPTU', null=True, blank=True)

    def create_status(self):
        status = StatusDocumentosRequerimentoISS(requerimento=self.requerimento)
        status.save()
        return status
    
class StatusDocumentosRequerimentoISS(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)

    rg_status=models.CharField(max_length=1, verbose_name='Status do RG', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_rg = models.ForeignKey(Agente_Tributario, related_name="rg_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status do RG", null=True)

    comprovante_endereco_status=models.CharField(max_length=1, verbose_name='Status do comprovante de endereço', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_endereco = models.ForeignKey(Agente_Tributario, related_name="comprovante_endereco_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status do comprovante de endereço", null=True)

    diploma_ou_certificado_status=models.CharField(max_length=1, verbose_name='Status do diploma ou certificado', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_certificado = models.ForeignKey(Agente_Tributario, related_name="certificado_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status do Certificado/Diploma", null=True)

    #Comum com Meio Ambiente
    espelho_iptu_status = models.CharField(max_length=1, verbose_name='Status Licenca Sanitária Anterior', choices=DOC_STATUS_CHOICES, default='0')    

    def validate_status(self):
        documentos = DocumentosRequerimentoISS.objects.filter(requerimento=self.requerimento).first()
        print(self.comprovante_endereco_status == '1' )
        if documentos:
            if documentos.espelho_iptu:
                if self.rg_status == '1' and self.comprovante_endereco_status == '1' and self.diploma_ou_certificado_status == '1' and self.espelho_iptu_status == '1':
                    return True                                
            else:
                if self.rg_status == '1' and self.comprovante_endereco_status == '1' and self.diploma_ou_certificado_status == '1':
                    return True                
        return False
    
class DocumentosLicencaAmbiental(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)

    licenca_ambiental = models.FileField(upload_to='processos/licenca_ambiental/', verbose_name='Licença ambiental', null=True, blank=True)
    
    contrato_locacao = models.FileField(upload_to='processos/contrato-locacao/', verbose_name='Cópia do contrato de locação, se houver', null=True, blank=True)
    conta_dagua = models.FileField(upload_to='processos/conta-dagua/', verbose_name="Conta d'água", null=True, blank=True)
    conta_luz = models.FileField(upload_to='processos/conta-luz/', verbose_name='Conta de luz', null=True, blank=True)
    foto = LimitedImageField(upload_to='processos/fotos_empresa/', null=True, blank=True, verbose_name="Foto da empresa para possibilitar a vistoria do técnico (jpg ou png)", help_text='Limite: 2MB', allowed_formats=['jpeg', 'jpg', 'png'], max_size=(2048, 2048))
    croqui_acesso = LimitedImageField(upload_to='processos/croqui_acesso/', null=True, blank=True, verbose_name="Croqui de acesso para possibilitar a localização e vistoria da local de atuação. (jpg ou png)", help_text='Limite: 2MB', allowed_formats=['jpeg', 'jpg', 'png'], max_size=(2048, 2048))

    def create_status(self):
        status = StatusDocumentosLicencaAmbiental(requerimento=self.requerimento)
        status.save()
        return status   
    
class StatusDocumentosLicencaAmbiental(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)
    
    contrato_locacao_status = models.CharField(max_length=1, verbose_name='Status do contrato de locação', choices=DOC_STATUS_CHOICES, default='0')    
    agente_att_contrato_locacao = models.ForeignKey(Agente_Sanitario, related_name="agente_contrato_locacao_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status do contrato de locação", null=True)

    conta_dagua_status = models.CharField(max_length=1, verbose_name='Status conta dagua', choices=DOC_STATUS_CHOICES, default='0')    
    agente_att_conta_dagua = models.ForeignKey(Agente_Sanitario, related_name="agente_conta_dagua_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da conta dagua", null=True)

    conta_luz_status = models.CharField(max_length=1, verbose_name='Status conta de luz', choices=DOC_STATUS_CHOICES, default='0')    
    agente_att_conta_luz = models.ForeignKey(Agente_Sanitario, related_name="agente_conta_luz_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da conta de luz", null=True)

    foto_status = models.CharField(max_length=1, verbose_name='Status da foto', choices=DOC_STATUS_CHOICES, default='0')    
    agente_att_foto = models.ForeignKey(Agente_Sanitario, related_name="agente_foto_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da foto da empresa", null=True)

    croqui_acesso_status = models.CharField(max_length=1, verbose_name='Status Licenca Sanitária Anterior', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_croqui = models.ForeignKey(Agente_Sanitario, related_name="agente_croqui_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da manutenção do ar", null=True)

class DocumentosLicencaSanitaria(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)

    licenca_sanitaria = models.FileField(upload_to='processos/licenca_sanitaria/', verbose_name='Licença sanitária', null=True, blank=True)

    comprovante_ar_condicionado = models.FileField(upload_to='processos/licenca_sanitaria/', verbose_name="Comprovante de manutenção de ar condicionado", null=True, blank=True)        
    comprovante_limpeza_caixa_dagua = models.FileField(upload_to='processos/licenca_sanitaria/', verbose_name="Laudo de serviço e comprovante de limpeza de caixa d'agua por firma credenciada no INEA", null=True, blank=True)   
    plano_gerenciamento_de_residuos = models.FileField(upload_to='processos/licenca_sanitaria/', verbose_name="Plano de ferenciamento de resíduos", null=True, blank=True)    
    licenca_santinaria_anterior = models.FileField(upload_to='processos/licenca_sanitaria/', verbose_name="Licença sanitária anterior (para renovação)", null=True, blank=True)
    
    def create_status(self):
        status = StatusDocumentosLicencaSanitaria(requerimento=self.requerimento)
        status.save()
        return status
    
class StatusDocumentosLicencaSanitaria(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)
    
    comprovante_ar_condicionado_status = models.CharField(max_length=1, verbose_name='Status Comprovante Ar Condicionado', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_ar_condicionado = models.ForeignKey(Agente_Sanitario, related_name="agente_ar_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da manutenção do ar", null=True)

    comprovante_limpeza_caixa_dagua_status = models.CharField(max_length=1, verbose_name="Status Limpeza Caixa d'Agua", choices=DOC_STATUS_CHOICES, default='0')
    agente_att_caixa_comprovante_limpeza_caixa_dagua = models.ForeignKey(Agente_Sanitario, related_name="agente_caixa_dagua_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da caixa d'água", null=True)
            

    plano_gerenciamento_de_residuos_status = models.CharField(max_length=1, verbose_name='Status Gerenciamento de Resíduos', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_plano_gerenciamento_de_residuos= models.ForeignKey(Agente_Sanitario, related_name="agente_residuos_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status do plano de resíduos", null=True)

    licenca_santinaria_anterior_status = models.CharField(max_length=1, verbose_name='Status Licenca Sanitária Anterior', choices=DOC_STATUS_CHOICES, default='0')
    agente_att_licenca_sanitaria_anterior = models.ForeignKey(Agente_Sanitario, related_name="agente_licenca_sanitaria_anexos", on_delete=models.CASCADE, verbose_name="Agente que autalizou o status da antiga licença sanitária", null=True)

class Relatorios(models.Model):
    processo = models.ForeignKey(Processo_Digital, on_delete=models.CASCADE, verbose_name='Processo', null=True)

    user = models.ForeignKey(Agente, on_delete=models.CASCADE, verbose_name='Agente', null=True)
    dt_register = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')
    descricao = models.TextField(verbose_name='Texto')
    aprovado = models.BooleanField(default=False, verbose_name='Aprovado?')
    
    def outros_agentes(self):
        agentes = AgentesRelatorios.objects.filter(relatorio=self, aprovado = True)
        print(agentes)
        print(agentes.exclude(agente=self.user))
        html = ''''''
        for agente in agentes.exclude(agente=self.user):
            html +=f'''<p class='outros-agentes'><strong>{agente.agente.pessoa.nome}</strong></p>    
'''     
        print(html)
        return html
    
    def get_descricao(self):
        descricao = self.descricao
        # Divide a descrição em partes usando a expressão regular que inclui um ou mais \n
        partes = re.split(r'(\n+)', descricao)

        # Processa cada parte para adicionar os parágrafos e as quebras de linha adequadas
        conteudo_formatado = ""
        for parte in partes:
            if '\n' in parte:
                num_quebras = len(parte)
                conteudo_formatado += '<br>' * (num_quebras - 1)  # -1 porque uma quebra já é convertida em um parágrafo
            else:
                conteudo_formatado += f'<p class="text-justify">{parte.strip()}</p>'

        return format_html(conteudo_formatado)

class BoletosRequerimentoISS(models.Model):
    requerimento = models.ForeignKey(RequerimentoISS, on_delete=models.CASCADE, verbose_name='Requerimento', null=True)
    boleto_requerimento = models.FileField(upload_to='processos/boletos/', verbose_name='Boleto Requerimento', null=True, blank=True)
    boleto_licenca_ambiental = models.FileField(upload_to='processos/boletos/', verbose_name='Boleto Licença Ambiental', null=True, blank=True)
    comprovante_licenca_ambiental = models.FileField(upload_to='processos/boletos/', verbose_name='Comprovante de pagamento da Licença Ambiental', null=True, blank=True)
    status_boleto_ambiental = models.BooleanField(default=False, verbose_name='Boleto Licença Ambiental Pago?')
    boleto_licenca_sanitaria = models.FileField(upload_to='processos/boletos/', verbose_name='Boleto Licença Sanitária', null=True, blank=True)
    comprovante_licenca_sanitaria = models.FileField(upload_to='processos/boletos/', verbose_name='Comprovante de pagamento da Licença Sanitária', null=True, blank=True)
    status_boleto_sanitario = models.BooleanField(default=False, verbose_name='Boleto Licença Sanitária Pago?')
  
class AgentesRelatorios(models.Model):
    relatorio = models.ForeignKey(Relatorios, on_delete=models.CASCADE, verbose_name='Relatório', null=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, verbose_name='Agente', null=True)
    aprovado = models.BooleanField(default=False, verbose_name='Aprovado?')
    dt_register = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro', null=True)
    
    def __str__(self):
        return f'{self.relatorio.processo} - {self.agente.pessoa.nome}'
    
    class Meta:
        verbose_name = 'Agente Relatório'
        verbose_name_plural = 'Agentes Relatórios'
    