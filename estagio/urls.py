from django.contrib import admin
from django.urls import path

from . import views

app_name = 'estagio'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('vagas/', views.vagas, name='vagas'),
    path('cadidato/', views.listar_candidato, name='candidato'),
    path('estagiario/', views.listar_estagiario, name='estagiario')
]
