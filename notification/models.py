from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.
ICONS_CHOICES=(
    ('<i class="text-success fa-solid fa-list-check my-auto me-4"></i>', 'Checkin icon'),
    ('<i class="fa-solid fa-file-invoice-dollar"></i>', 'Payment icon'),
)

class Notification(models.Model):

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'

    def __str__(self):
        return f'{self.referencia} - {self.mensagem}'

    for_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário que deve ser notificado')
    icone = models.CharField(max_length=150, choices=ICONS_CHOICES, verbose_name='Qual icone deve ser exibido?')    
    referencia = models.CharField(max_length=40, verbose_name='Qual é a referência? Referência é o texto menor na notificação.')
    mensagem = models.CharField(max_length=36,verbose_name='Qual mensagem deve ser exibida?')
    url_redirect = models.CharField(max_length=150, verbose_name='Qual URL deve ser redirecionada?')
    hash = models.CharField(max_length=150, verbose_name='Hash da notificação', null=True, blank=True)
    viewed = models.BooleanField(default=False, verbose_name='Visualizado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    def save(self, *args, **kwargs):
        if not self.hash:
            hash_string = f"{self.for_user.id}{self.referencia}{self.mensagem}{self.url_redirect}"
            self.hash = hashlib.sha256(hash_string.encode()).hexdigest()
        super().save(*args, **kwargs)
