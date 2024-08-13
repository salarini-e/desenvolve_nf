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
    return render(request, 'forms/pca/listagem_pca.html', {'cadastros': cadastros})

import os
import subprocess
from django.http import HttpResponse
from django.conf import settings
from django.views import View

class BackupDatabaseView(View):
    def get(self, request):
        # Caminho para salvar o backup localmente
        backup_file_path = os.path.join(settings.BASE_DIR, 'backup', 'desenvolve_nf_atual_backup.sql')

        # Detalhes do banco de dados a partir das variáveis de ambiente
        db_name = settings.db_name['db_name']
        db_user = settings.db_user['db_user']
        db_host = settings.db_host['db_host']
        db_port = settings.db_port['db_port']
        db_passwd = settings.db_passwd['db_pw']

        # Comando mysqldump para servidor remoto
        command = f"mysqldump -h {db_host} -P {db_port} -u {db_user} -p'{db_passwd}' {db_name} > {backup_file_path}"

        # Executar o comando
        subprocess.run(command, shell=True, check=True)

        # Retornar o arquivo de backup
        with open(backup_file_path, 'rb') as backup_file:
            response = HttpResponse(backup_file.read(), content_type='application/sql')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(backup_file_path)}'
            return response