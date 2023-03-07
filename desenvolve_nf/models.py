from django.db import models

# Create your models here.
class Carousel_Index(models.Model):
    
    nome = models.CharField(max_length=64, verbose_name="Nome para identificação ou para texto alternativo", blank=False, null=False)
    image = models.ImageField(upload_to='carousel_index/', verbose_name="Imagem 987x394", blank=False, null=True)
    ativa = models.BooleanField(default=True)
    
    def __str__(self):
        return '%s - %s' % (self.nome, self.id)