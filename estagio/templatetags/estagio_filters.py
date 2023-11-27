from django import template
from datetime import date
import locale
from ..models import Estudante_Vaga
register = template.Library()

@register.filter(name='contarEstagiarios')
def contarEstagiario(value):
    valor = Estudante_Vaga.objects.filter(status='1', local_do_estagio__secretaria__id=value).count()
    return valor
