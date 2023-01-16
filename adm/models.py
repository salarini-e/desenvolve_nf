from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Layout(models.Model):

    nome_instituicao = models.CharField(max_length=150, verbose_name="Nome da instituição")
    logo = models.ImageField()
    logo_grande =  models.ImageField()        

    dt_inclusao = models.DateField(auto_now_add=True, editable=False)    
    user_inclusao = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return 'Clica aqui para alterar o layout'