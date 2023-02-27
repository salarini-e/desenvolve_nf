from django import template
from ..models import Candidato
register = template.Library()

@register.filter
def qntcandidatos(obj):       
    try:
        candidatos=Candidato.objects.filter(vaga=obj)
        return str(len(candidatos))
    except:
        return None
