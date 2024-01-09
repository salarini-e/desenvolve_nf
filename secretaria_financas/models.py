from django.db import models
from autenticacao.models import User

class Setor(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Funcionarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    dt_register = models.DateTimeField(auto_now_add=True)
    user_register = models.ForeignKey(User, related_name='user_register', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome