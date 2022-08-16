from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('cursos/', views.cursos, name="cursos"),
    path('prematricula/', views.prematricula, name="prematricula"),
    path('alterarCadastro/', views.alterarCad, name="alterarCad"),
    path('resultado/', views.resultado, name="resultado"),
]