from .models import Servidor_Recadastramento

def is_servidor(pessoa):
    return Servidor_Recadastramento.objects.filter(user=pessoa).exists()