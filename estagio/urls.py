from django.contrib import admin
from django.urls import path

from . import views

app_name = 'estagio'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('vagas/', views.vagas, name='vagas'),
    path('cadidato/', views.listar_candidato, name='candidato'),
    path('estagiario/', views.listar_estagiario, name='estagiario'),
    path('vagas/<id>/canditar-se/', views.candidatar_se_vaga, name='candidatar_se_vaga'),
    path('candidato/<id>/editar/', views.editar_estudante, name='editar_candidato'),
    path('vagas/cadastrar/', views.cadastro_vaga, name='cadastro_vaga'),

]
