from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CadastroPCA
from .forms import CadastroPCAForm

@login_required
def criar_cadastro_pca(request):
    if request.method == 'POST':
        form = CadastroPCAForm(request.POST)
        if form.is_valid():
            cadastro_pca = form.save(commit=False)
            cadastro_pca.user = request.user  # Atribui o usuário autenticado
            cadastro_pca.save()
            return redirect('forms:lista_cadastros_pca')  # Redireciona para a lista de cadastros após salvar
    else:
        form = CadastroPCAForm(initial={'user': request.user})

    return render(request, 'forms/pca/cadastro_pca.html', {'form': form})

@login_required
def editar_cadastro_pca(request, pk):
    cadastro_pca = get_object_or_404(CadastroPCA, pk=pk)
    
    if request.user != cadastro_pca.user:
        return redirect('forms:lista_cadastros_pca')  # Redireciona se o usuário não for o dono do cadastro

    if request.method == 'POST':
        form = CadastroPCAForm(request.POST, instance=cadastro_pca)
        if form.is_valid():
            form.save()
            return redirect('forms:lista_cadastros_pca')
    else:
        form = CadastroPCAForm(instance=cadastro_pca)

    return render(request, 'forms/pca/cadastro_pca.html', {'form': form})

@login_required
def lista_cadastros_pca(request):
    cadastros = CadastroPCA.objects.filter(user=request.user)
    return render(request, 'forms/pca/listagem_pca.html', {'cadastros': cadastros, 'titulo': 'Plano de Compras Anual'})

import os
import subprocess
from django.http import HttpResponse
from django.conf import settings
from settings.settings import db_name, db_user, db_host, db_port, db_passwd
from django.views import View

class BackupDatabaseView(View):
    def get(self, request):
        # Caminho para salvar o backup localmente
        backup_file_path = os.path.join(settings.MEDIA_ROOT, f'{db_name}_backup.sql')

        command = [
            'mysqldump',
            '-h', db_host,
            '-P', db_port,
            '-u', db_user,
            f'--password={db_passwd}',
            db_name
        ]

        try:
            # Executando o comando e salvando o backup no arquivo
            with open(backup_file_path, 'w') as backup_file:
                subprocess.run(command, stdout=backup_file, check=True)

            # Retornar o arquivo de backup como resposta para download
            with open(backup_file_path, 'rb') as backup_file:
                response = HttpResponse(backup_file.read(), content_type='application/sql')
                response['Content-Disposition'] = f'attachment; filename={os.path.basename(backup_file_path)}'
                return response

        except subprocess.CalledProcessError as e:
            # Lidar com erros durante o backup
            return HttpResponse(f"Erro ao criar backup: {str(e)}", status=500)