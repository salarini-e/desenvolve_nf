from django import template
from datetime import date
import locale
from ..models import OS_Linha_Tempo
register = template.Library()

# Função para obter o nome do mês por extenso em português
@register.filter(name='mes_extenso')
def mes_extenso(value):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    return value.strftime('%d de %B de %Y')

@register.filter(name='qntMsg')
def qntMsg(value):
    qnt_msg=OS_Linha_Tempo.objects.filter(os_id=value).count()
    return qnt_msg