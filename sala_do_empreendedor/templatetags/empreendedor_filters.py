from django import template
from datetime import date
import locale
from ..models import Solicitacao_de_Compras, Item_Solicitacao, Proposta_Item
register = template.Library()

@register.filter(name='contarProcessos')
def contarProcessos(value):
    valor = Solicitacao_de_Compras.objects.filter(status__in=['0', '1' , '2'], escola=value).count()
    return valor

@register.filter(name='contarItensProcessos')
def contarItensProcessos(value):
    valor = Item_Solicitacao.objects.filter(solicitacao_de_compra__id=value).count()
    return valor

@register.filter(name='limitarCaracteres')
def limitarCaracteres(value, qnt):
    qnt_caracteres=len(value)
    if qnt_caracteres > qnt:
        valor = value[:qnt] + '...'
    else:
        valor = value
    return valor

@register.filter(name='contarPropostas')
def contarPropostas(value):
    valor = Proposta_Item.objects.filter(item_solicitacao__id=value).count()
    return valor

@register.filter(name='formatarPreco')
def formatarPreco(value):
    valor = '{:,.2f}'.format(value / 100).replace('.', '##').replace(',', '.').replace('##', ',')
    return valor