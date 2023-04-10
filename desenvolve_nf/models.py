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
    madrugada = models.CharField(verbose_name="Clima na madrugada", max_length=50, blank=True)
    manha = models.CharField(verbose_name="Clima na manhã", max_length=50, blank=True)
    tarde = models.CharField(verbose_name="Clima na tarde", max_length=50, blank=True)
    noite = models.CharField(verbose_name="Clima na noite", max_length=50, blank=True)
    dt_inclusao = models.DateTimeField( auto_now_add=True, unique=True)

    IMAGEM_URL={
                'sol com muitas nuvens':                '/static/images/clima_icons/sol_nuvem_vento.png',
                'sol, pancadas de chuva e trovoadas':   '/static/images/clima_icons/chuva_tempestade.png',
                'noite com muitas nuvens':              '/static/images/clima_icons/noite_nuvem.png',
                'noite nublada com chuva':              '/static/images/clima_icons/#',

                'erro':                                 '/static/images/Screen.png',
                }

    class Meta:
        ordering = ['-dt_inclusao']
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios de clima"


    def getImg(self, turno):
        if turno == "madrugada":
            return self.IMAGEM_URL[self.madrugada]
        elif turno == "manha":
            return self.IMAGEM_URL[self.manha]
        elif turno == "tarde":
            return  self.IMAGEM_URL[self.tarde]
        elif turno == "noite":
            return  self.IMAGEM_URL[self.Noite]
        else:
            return self.IMAGEM_URL['erro']
    
    def turno(self):
        TURNOS={
                'madrugada': [0,6],
                'manha':     [6,12],
                'tarde':     [12,18],
                'noite':     [18,00]
        }
        hora = int(self.dt_inclusao.strftime('%H'))-3
        for i in TURNOS:
            if hora >= TURNOS[i][0] and hora < TURNOS[i][1]:
                return i
            
    def timeBeholder(self):
        turno = self.turno()
        try:
            return self.getImg(turno)
        except:
            return self.IMAGEM_URL['erro']