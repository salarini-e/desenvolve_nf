from django.db import models

# Create your models here.

# class Empresa(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField()
#     contato = models.CharField(max_length=100)

# class Produto(models.Model):
#     nome = models.CharField(max_length=100)
#     descricao = models.TextField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     imagem = models.ImageField(upload_to='produtos/')
#     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)