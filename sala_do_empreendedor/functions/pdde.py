import locale
from django.db import connection
from ..models import Item_Solicitacao, Empresa, Contrato_de_Servico
from ..forms import Criar_Item_Solicitacao

def Calcula_Melhor_Proposta(solicitacao):

    locale.setlocale(locale.LC_ALL, '')
    soma = {'menor_valor':0, 'maior_valor':0}
    itens=Item_Solicitacao.objects.filter(solicitacao_de_compra=solicitacao)
    itens_valores=[]
    for item in itens:
        query_menor = f"SELECT MIN(preco), empresa_id FROM sala_do_empreendedor_proposta_item WHERE item_solicitacao_id = {item.id};"
        query_maior = f"SELECT MAX(preco), empresa_id FROM sala_do_empreendedor_proposta_item WHERE item_solicitacao_id = {item.id};"

        with connection.cursor() as cursor:
            cursor.execute(query_menor)
            dados = cursor.fetchone()
            menor_valor = dados[0]
            menor_empresa_id = dados[1]
            soma['menor_valor'] += menor_valor
            cursor.execute(query_maior)
            dados = cursor.fetchone()
            maior_valor = dados[0]
            maior_empresa_id = dados[1]
            soma['maior_valor'] += maior_valor
        
        try:
            formato_menor_valor_unidade = '{:,.2f}'.format(menor_valor/(item.quantidade * 100)).replace('.', '##').replace(',', '.').replace('##', ',')
        except:
            formato_menor_valor_unidade='0,00'
        try:
            formato_menor_valor = '{:,.2f}'.format(menor_valor / 100).replace('.', '##').replace(',', '.').replace('##', ',')
        except:
            formato_menor_valor='0,00'
        try:
            formato_maior_valor_unidade = '{:,.2f}'.format(maior_valor/(item.quantidade * 100)).replace('.', '##').replace(',', '.').replace('##', ',')
        except:
            formato_maior_valor_unidade='0,00'
        try:
            formato_maior_valor = '{:,.2f}'.format(maior_valor / 100).replace('.', '##').replace(',', '.').replace('##', ',')
        except:
            formato_maior_valor='0,00'
        
        try:
            empresa_menor=Empresa.objects.get(id=menor_empresa_id).nome
        except:
            empresa_menor='Nenhuma proposta realizada.'
        try:
            empresa_maior=Empresa.objects.get(id=maior_empresa_id).nome
        except:
            empresa_maior='Nenhuma proposta realizada.'
            
        itens_valores.append([item, [f'{formato_menor_valor_unidade}', formato_menor_valor], empresa_menor, [f'{formato_maior_valor_unidade}', formato_maior_valor], empresa_maior, item.solicitacao_de_compra.id, item.id])
    return  itens_valores, soma 

# def Calcula_Melhor_Proposta(solicitacao):
#     locale.setlocale(locale.LC_ALL, '')
#     soma = {'menor_valor':0, 'maior_valor':0}
#     itens=Item_Solicitacao.objects.filter(solicitacao_de_compra=solicitacao)
#     itens_valores=[]
#     for item in itens:
#         query_menor = f"SELECT MIN(preco), empresa_id FROM sala_do_empreendedor_proposta_item WHERE item_solicitacao_id = {item.id};"
#         query_maior = f"SELECT MAX(preco), empresa_id FROM sala_do_empreendedor_proposta_item WHERE item_solicitacao_id = {item.id};"

#         with connection.cursor() as cursor:
#             cursor.execute(query_menor)
#             dados = cursor.fetchone()
#             menor_valor = dados[0]
#             menor_empresa_id = dados[1]
#             soma['menor_valor'] += menor_valor
            
#             cursor.execute(query_maior)
#             dados = cursor.fetchone()
#             maior_valor = dados[0]
#             maior_empresa_id = dados[1]
#             soma['maior_valor'] += maior_valor
        
#         try:
#             formato_menor_valor_unidade = '{:,.2f}'.format(menor_valor/(item.quantidade * 100)).replace('.', '##').replace(',', '.').replace('##', ',')
#         except:
#             formato_menor_valor_unidade='0,00'
#         try:
#             formato_menor_valor = '{:,.2f}'.format(menor_valor / 100).replace('.', '##').replace(',', '.').replace('##', ',')
#         except:
#             formato_menor_valor='0,00'
#         try:
#             formato_maior_valor_unidade = '{:,.2f}'.format(maior_valor/(item.quantidade * 100)).replace('.', '##').replace(',', '.').replace('##', ',')
#         except:
#             formato_maior_valor_unidade='0,00'
#         try:
#             formato_maior_valor = '{:,.2f}'.format(maior_valor / 100).replace('.', '##').replace(',', '.').replace('##', ',')
#         except:
#             formato_maior_valor='0,00'
        
#         try:
#             empresa_menor=Empresa.objects.get(id=menor_empresa_id).nome
#         except:
#             empresa_menor='Nenhuma proposta realizada.'
#         try:
#             empresa_maior=Empresa.objects.get(id=maior_empresa_id).nome
#         except:
#             empresa_maior='Nenhuma proposta realizada.'
            
#         itens_valores.append([item, [f'{formato_menor_valor_unidade}', formato_menor_valor], empresa_menor, [f'{formato_maior_valor_unidade}', formato_maior_valor], empresa_maior, item.solicitacao_de_compra.id, item.id])
#     return  itens_valores, soma

def Criar_Contrato(solicitacao):
    print('fazer tela do contrato')
    # Contrato_de_Servico.objects.create(solicitacao_de_compra=solicitacao)
    return 'contrato-criado'

def Aceitar_Proposta(solicitacao):
    solicitacao.status='3'
    solicitacao.save()
    response =  Criar_Contrato(solicitacao)
    if response == 'contrato-criado':
        return 'proposta-aceita'
    else:
        return 'erro'

def PDDE_POST(request, solicitacao):
    if solicitacao.escola.ativa:
        if solicitacao.status == '0':
            solicitacao.status='1'
            solicitacao.save()
            return 'salvo'
        else:
            response = Aceitar_Proposta(solicitacao)
            return response
    else:
        return 'escola-inativa'



def Divulgar_Vencedor(solicitacao):
    return 'envi'

def Enviar_Contrato(solicitacao):
    return 'envi'