from django.db import models

# Create your models here.
class Tipo_Material(models.Model):
    nome=models.CharField('Tipo de Material', max_length=120)
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    class Meta:
        verbose_name_plural = "Tipos de Materiais"
        verbose_name = "Tipo de Material"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Material(models.Model):
    tipo=models.ForeignKey(Tipo_Material, on_delete=models.CASCADE)
    nome=models.CharField('Nome do Material', max_length=120)
    qnt_em_estoque=models.IntegerField(default=0, blank=True, null=True)
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    class Meta:
        verbose_name_plural = "Materiais"
        verbose_name = "Material"
        ordering = ['tipo__nome','nome', 'qnt_em_estoque']
    
    def __str__(self):
        return self.nome

class Log_estoque(models.Model):
    material=models.ForeignKey(Material, on_delete=models.CASCADE)
    add_quantidade=models.IntegerField(verbose_name='Quantidade p/ adicionar ao estoque')
    qnt_em_estoque=models.IntegerField(null=True)
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')    
    
    class Meta:
        verbose_name_plural = "Log do estoque dos materiais"
        verbose_name = "Log do estoque do material"
        ordering = ['material__nome']

# class Estoque(models.Model):
#     material=models.ForeignKey(Material, on_delete=models.CASCADE)
#     quantidade=models.IntegerField()
#     dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')    
    
#     class Meta:
#         verbose_name_plural = "Estoque dos Materiais"
#         verbose_name = "Estoque do Material"
#         ordering = ['material__nome']
