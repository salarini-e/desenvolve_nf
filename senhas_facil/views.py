from django.shortcuts import render
from django.db import connections
import json
from django.http import JsonResponse
from datetime import datetime

def fetch_data_from_senhas_db(query, params=None):
    with connections['senhas_facil_b'].cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

def get_posicao_na_fila(tipo_atendimento_prefixo, numero_senha):
    hoje = datetime.now().date()

    
    query_status = f"""
        SELECT a.status_atendimento, DATE(a.data_atendimento)
        FROM atendimento_atendimento a
        JOIN atendimento_tipoatendimento t ON a.tipo_atendimento_id = t.id
        WHERE t.prefixo=%s
        AND a.numero_senha=%s
        ORDER BY a.data_atendimento DESC
        LIMIT 1
    """
    params = [tipo_atendimento_prefixo, numero_senha]
    result_status = fetch_data_from_senhas_db(query_status, params)
    if not result_status or result_status[0][1] != hoje:
        return 0, 'não encontrado'

    status = result_status[0][0]

    
    query_posicao = f"""
        SELECT COUNT(*)
        FROM atendimento_atendimento a
        JOIN atendimento_tipoatendimento t ON a.tipo_atendimento_id = t.id
        WHERE a.status_atendimento='fila'
        AND t.prefixo=%s
        AND a.numero_senha < %s
        AND DATE(a.data_atendimento) = %s
    """
    params_posicao = [tipo_atendimento_prefixo, numero_senha, hoje]
    result_posicao = fetch_data_from_senhas_db(query_posicao, params_posicao)

    posicao = result_posicao[0][0] + 1 if status == 'fila' else 0
    return posicao, status

def posicao_na_fila(request):
    resultado = None
    context = {}
    if request.method == 'POST':
        try:
            senha = request.POST.get('senha')
            tipo_atendimento_prefixo = senha[0]  # Extrai o prefixo do tipo de atendimento
            numero_senha = int(senha[1:])  # Extrai o número da senha
            posicao, status = get_posicao_na_fila(tipo_atendimento_prefixo, numero_senha)
            resultado = {
                'senha': senha,
                'posicao_na_fila': posicao,
                'status': status
            }
        except:
            context['error'] = 'Houve um problema ao processar a posição dessa senha na fila.'
        context['resultado'] = resultado
    return render(request, 'senha_facil/celular_senhas_chamadas.html', context)


def fetch_posicao_na_fila(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            senha = data.get('senha')
            tipo_atendimento_prefixo = senha[0]
            numero_senha = int(senha[1:])
            posicao, status = get_posicao_na_fila(tipo_atendimento_prefixo, numero_senha)
            return JsonResponse({
                'senha': senha,
                'posicao_na_fila': posicao,
                'status': status
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)