from django.urls import path
from . import views
 
app_name='iluminacao'
urlpatterns = [
    # path('', views.index, name='os_index'),
    path('', views.os_index, name='os_index'),
    path('os/', views.add_os, name='add_os'),

    path('os/painel/<id>/', views.detalhes_os, name='detalhes_os'),
    path('os/painel/<id>/atender', views.atender_os, name='atender_os'),

    path('funcionario', views.funcionarios_listar, name='funcionarios'),
    path('funcionario/cadastrar/', views.funcionario_cadastrar, name='cadastrar funcionario'),
    path('funcionario/editar/<id>/', views.funcionario_editar, name='editar funcionario'),
    path('funcionario/deletar/<id>/', views.funcionario_deletar, name='deletar funcionario'),

    path('os/painel/<id>/equipe/', views.atribuir_equipe, name='atribuir equipe')
]