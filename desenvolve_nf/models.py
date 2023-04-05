from django.db import models

# Create your models here.
class Carousel_Index(models.Model):
    
    nome = models.CharField(max_length=64, verbose_name="Nome para identificação ou para texto alternativo", blank=False, null=False)
    image = models.ImageField(upload_to='carousel_index/', verbose_name="Imagem 987x394", blank=False, null=True)
    url = models.CharField(max_length=64, verbose_name="Url, caso tenha para redirecionar", blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.nome, self.id)
    

class ClimaTempo(models.Model):
    maxTemp = models.CharField(verbose_name="Temperatura máxima", max_length=3)
    minTemp = models.CharField(verbose_name="Temperatura mínima", max_length=3)
    madrugada = models.CharField("Clima na madrugada", max_length=50)
    manha = models.CharField(verbose_name="Clima na manhã", max_length=50)
    tarde = models.CharField(verbose_name="Clima na tarde", max_length=50)
    noite = models.CharField(verbose_name="Clima na noite", max_length=50)
    dt_inclusao = models.DateTimeField( auto_now_add=True, unique=True)

    IMAGEM_URL={
                'sol com muitas nuvens':    'static/icones_tempo/nublado.png',
                'erro':                     '#',
                }

    class Meta:
        ordering = ['-dt_inclusao']
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios de clima"

