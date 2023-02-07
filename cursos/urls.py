from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('cursos/', views.cursos, name="cursos"),        
    
    # path('cursos/cadastrar-categoria', views.cadastrar_categoria, name="cadastrar_categoria"),
    # path('cursos/cadastrar-local', views.cadastrar_local, name="cadastrar_local"),
    
    path('prematricula/', views.prematricula, name="prematricula"),
    path('alterarCadastro/', views.alterarCad, name="alterarCad"),
    path('resultado/', views.resultado, name="resultado"),

    #API
    path('login/', views.login_view, name='login'),  
]