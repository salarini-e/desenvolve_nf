from django.shortcuts import render
from .forms import PessoaRecadastramentoForm, ProcessoForm, InscricaoForm
from .models import PessoaRecadastramento
from django.views.decorators.csrf import csrf_exempt
import json
from autenticacao.functions import validate_cpf
from django.http import JsonResponse
from django.core.exceptions import ValidationError

def index(request):
    context = {
        'titulo': 'Sala do Empreendedor - Serviços Internos',
        'form_pessoa_recadastramento': PessoaRecadastramentoForm(),
        'form_processo': ProcessoForm(),
        'form_inscricao': InscricaoForm(),
    }
    return render(request, 'recadastramento/index.html', context)


def checkCPF(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cpf = data.get('cpf')
        try:
            cpf = validate_cpf(cpf)
        except:
            response_data = {'exists': True, 'message': 'CPF inválido.'}
            return JsonResponse(response_data)
        try:
            pessoa = PessoaRecadastramento.objects.get(cpf=cpf)
            response_data = {'exists': True, 'message': 'CPF já existe no recadastramento.'}
        except:
                response_data = {'exists': False}

        return JsonResponse(response_data)
    return JsonResponse({})

def checkCPF2(request):    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cpf = data.get('cpf')
        try:
            cpf = validate_cpf(cpf)
        except:
            response_data = {'exists': False, 'message': 'CPF inválido.'}
            return JsonResponse(response_data)
        try:
            pessoa = PessoaRecadastramento.objects.get(cpf=cpf)
            response_data = {'exists': True, 'message': 'Contribuinte localizado <i class="fa-solid fa-circle-check"></i>'}
        except:
                response_data = {'exists': False, 'message': 'Contribuinte não localizado <i class="fa-solid fa-circle-xmark"></i>'}

        return JsonResponse(response_data)
    return JsonResponse({})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaRecadastramentoForm(request.POST)
        if form.is_valid():
            form.save()
    return index(request)


@csrf_exempt
def cadastrar_pessoa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            pessoa = PessoaRecadastramento(
                cpf=data.get('cpf'),
                responsavel_tributario=data['responsavel_tributario'],
                cnpj=data.get('cnpj'),
                nome_do_contribuinte=data['nome_do_contribuinte'],
                celular=data.get('celular'),
                cep=data.get('cep'),
                rua=data.get('rua'),
                numero=data.get('numero'),
                complemento=data.get('complemento'),
                bairro=data.get('bairro'),
                cidade=data.get('cidade'),
                estado=data.get('estado'),
                email=data.get('email')
            )
            
            pessoa.full_clean()  # Valida os campos antes de salvar
            pessoa.save()
            
            return JsonResponse({'message': 'Cadastro realizado com sucesso!'}, status=201)
        except ValidationError as e:
            errors = e.message_dict
            return JsonResponse({'errors': errors}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)