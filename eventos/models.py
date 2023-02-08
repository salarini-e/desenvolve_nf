from django.db import models

# Create your models here.

class Evento(models.Model):
    DIAS_SEMANA_CHOICES = (
        ('1', 'Domingo'),
        ('2', 'Segunda-Feira'),
        ('3', 'Terça-Feira'),
        ('4', 'Quarta-Feira'),
        ('5', 'Quinta-Feira'),
        ('6', 'Sexta-Feira'),
        ('7', 'Sábado'),
    )

    titulo = models.CharField(max_length=64)
    subtitulo = models.CharField(max_length=64)

    data_inicio = models.DateField()
    data_fim = models.DateField()

    local = models.CharField(max_length=128)
    google_maps = models.URLField()
    idade_minima = models.IntegerField(
        verbose_name='Idade mínima', null=True, blank=True)
    idade_maxima = models.IntegerField(
        verbose_name='Idade máxima', null=True, blank=True)
    banner_file = models.ImageField(upload_to='banner_evento', verbose_name='Arte do evento')
    is_destaque = models.BooleanField(default=False)