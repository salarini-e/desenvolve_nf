from django.shortcuts import render
from .forms import PessoaRecadastramentoForm, ProcessoForm, InscricaoForm, _PessoaRecadastramentoForm
from .models import PessoaRecadastramento, Processo, Inscricao
from django.views.decorators.csrf import csrf_exempt
import json
from autenticacao.functions import validate_cpf
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.contrib.auth.decorators import login_required
from autenticacao.models import Pessoa
from django.http import HttpResponse

@login_required
def index(request):
    context = {
        'titulo': 'Sala do Empreendedor - Serviços Internos',
        'form_pessoa_recadastramento': PessoaRecadastramentoForm(),
        'form_processo': ProcessoForm(),
        'form_inscricao': InscricaoForm(),
    }
    return render(request, 'recadastramento/index.html', context)


@login_required
def atualziacao_cadastral(request):
    pessoa = Pessoa.objects.get(user = request.user)
    error = json.dumps({})
    try:        
        pessoaR = PessoaRecadastramento.objects.get(cpf=pessoa.cpf)
    except:
        pessoaR= pessoa

    if request.method == 'POST':
        try:
            instante =  PessoaRecadastramento.objects.get(cpf=pessoa.cpf)
            form = _PessoaRecadastramentoForm(request.POST, instance=instante)
        except:
            form = _PessoaRecadastramentoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            if 'n_inscricao' in request.POST:
                print(request.POST['n_inscricao'])
                print(request.POST.getlist('n_inscricao'))
                for i in request.POST.getlist('n_inscricao'):
                    inscricao = Inscricao(
                        pessoa_recadastramento=PessoaRecadastramento.objects.get(cpf=pessoa.cpf),
                        numero_inscricao=i
                    )
                    inscricao.full_clean()
                    inscricao.save()
            message = 'Cadastro atualizado com sucesso!'
            
        else:
            error = form.errors.as_json()
            message = 'Erro ao atualizar cadastro. Verifique os campos.'
            
    context = {
        'titulo': 'Sala do Empreendedor - Serviços Internos',        
        'pessoa': pessoaR,
        'error': error,
    }
    return render(request, 'recadastramento/tela_contribuinte.html', context)

@login_required
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
            pessoa = PessoaRecadastramento.objects.get(cpf=data.get('cpf'))
            pessoa_json = serializers.serialize('json', [pessoa])
            response_data = {'exists': True, 'message': 'CPF já existe. Confira os dados para atualizar.', 'pessoa': pessoa_json}
        except:
                response_data = {'exists': False}

        return JsonResponse(response_data)
    return JsonResponse({})

@login_required
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
            pessoa = PessoaRecadastramento.objects.get(cpf=data.get('cpf'))
            pessoa_json = serializers.serialize('json', [pessoa])
            response_data = {'exists': True, 'message': 'Contribuinte localizado <i class="fa-solid fa-circle-check"></i>', 'pessoa': pessoa_json}
        except:
            response_data = {'exists': False, 'message': 'Contribuinte não localizado <i class="fa-solid fa-circle-xmark"></i>'}

        return JsonResponse(response_data)
    return JsonResponse({})

# def cadastrar_pessoa(request):
#     if request.method == 'POST':
#         form = PessoaRecadastramentoForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return index(request)

@login_required
@csrf_exempt
def cadastrar_pessoa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            try:
                pessoa = PessoaRecadastramento.objects.get(cpf=data.get('cpf'))
                pessoa.cpf=data.get('cpf')
                pessoa.responsavel_tributario=data['responsavel_tributario']
                pessoa.cnpj=data.get('cnpj')
                pessoa.nome_do_contribuinte=data['nome_do_contribuinte']
                pessoa.celular=data.get('celular')
                pessoa.cep=data.get('cep')
                pessoa.rua=data.get('rua')
                pessoa.numero=data.get('numero')
                pessoa.complemento=data.get('complemento')
                pessoa.bairro=data.get('bairro')
                pessoa.cidade=data.get('cidade')
                pessoa.estado=data.get('estado')
                pessoa.email=data.get('email')
                message = 'Contribuinte atualizado com sucesso!'
            except:
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
                message = 'Cadastro realizado com sucesso!'
                
            pessoa.full_clean()  # Valida os campos antes de salvar
            pessoa.save()            
            return JsonResponse({'message': message}, status=201)
        except ValidationError as e:
            errors = e.message_dict
            return JsonResponse({'errors': errors}, status=400)
        except Exception as e:
            errors = e.message_dict
            return JsonResponse({'error': errors}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    

@login_required
@csrf_exempt
def cadastrar_processo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            processo = Processo(
                requerente=PessoaRecadastramento.objects.get(cpf=data.get('cpf_processo')),
                requerimento=data['requerimento'],
                ano=data.get('ano'),
                localizacao=data['localizacao'],                
            )            
            processo.full_clean()  # Valida os campos antes de salvar
            processo.save()
            
            return JsonResponse({'message': 'Cadastro realizado com sucesso!'}, status=201)
        except ValidationError as e:
            errors = e.message_dict
            return JsonResponse({'errors': errors}, status=400)
        except Exception as e:
            print(e)            
            errors = {
                'cpf_recadastramento': 'Erro ao cadastrar processo. Verifique se o contribuinte já foi cadastrado.'
            
            }
            return JsonResponse({'error': errors}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
@login_required    
@csrf_exempt
def cadastrar_inscricao(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            inscricao = Inscricao(
                pessoa_recadastramento=PessoaRecadastramento.objects.get(cpf=data.get('cpf_inscricao')),
                numero_inscricao=data['numero_inscricao'],                
            )         
            print(1)   
            inscricao.full_clean()  # Valida os campos antes de salvar
            print(2)
            inscricao.save()
            print(3)
            return JsonResponse({'message': 'Cadastro realizado com sucesso!'}, status=201)
        except ValidationError as e:
            errors = e.message_dict
            return JsonResponse({'errors': errors}, status=400)
        except Exception as e:
            print(e)            
            errors = {
                'cpf_inscricao': 'Erro ao cadastrar processo. Verifique se o contribuinte já foi cadastrado.'
            
            }
            return JsonResponse({'error': errors}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
@login_required
def cadastar_usuarios_no_recadastramento(request):
    pessoas = Pessoa.objects.all()
    ja_cadastrados = []
    for pessoa in pessoas:
        try:
            pessoa_recadastramento = PessoaRecadastramento(
                cpf=pessoa.cpf,
                nome_do_contribuinte=pessoa.nome,
                celular=pessoa.telefone,
                cep=pessoa.cep,
                rua=pessoa.endereco,
                numero=pessoa.numero,
                complemento=pessoa.complemento,
                bairro=pessoa.bairro,            
                email=pessoa.email
            )
            pessoa_recadastramento.full_clean()
            pessoa_recadastramento.save()
        except:
            ja_cadastrados.append(str(pessoa.nome)+';'+str(pessoa.cpf)+';')
    
    
    file_path = '/home/eduardo/Documentos/Github/desenvolve_nf (cópia)/financas_recadastramento/cadastrados.txt'
    
    with open(file_path, 'w') as file:
        for cadastrado in ja_cadastrados:
            file.write(cadastrado)
            file.write("\n")
        file.write("####")
        file.write("\n")
        file.write(f"total_cadastrados: {pessoas.count() - len(ja_cadastrados)}; total_que_já_estavam: {len(ja_cadastrados)};")
    
    with open(file_path, 'r') as file:
        response = HttpResponse(file.read(), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="cadastrados.txt"'
    
    return response

def listar_contribuintes(request):
    contribuintes = PessoaRecadastramento.objects.all()

    context={
        'contribuintes': contribuintes
    }

    return render(request, 'recadastramento/listar_contribuintes.html', context)