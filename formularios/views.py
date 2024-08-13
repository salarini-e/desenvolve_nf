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