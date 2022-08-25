from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('cursos/', views.cursos, name="cursos"),        
    
    path('cursos/listar-candidatos/<id>', views.listar_candidatos_curso, name="listar_candidatos_curso"),
    
    path('cursos/cadastrar-categoria', views.cadastrar_categoria, name="cadastrar_categoria"),
    path('cursos/cadastrar-local', views.cadastrar_local, name="cadastrar_local"),
    
    path('prematricula/', views.prematricula, name="prematricula"),
    path('alterarCadastro/', views.alterarCad, name="alterarCad"),
    path('resultado/', views.resultado, name="resultado"),
    #ADMINISTRATIVO
    path('administrativo/', views.administrativo, name="administrativo"),
        ##CURSOS
        path('administrativo/cursos/', views.adm_cursos, name="adm_cursos"),
        path('administrativo/cursos/cadastrar', views.cadastrar_curso, name="cadastrar_curso"),
        path('administrativo/cursos/listar', views.listar_cursos, name="adm_cursos_listar"),
        path('administrativo/cursos/editar/<id>', views.editar_curso, name="editar_curso"),
        ##TURMAS
        path('administrativo/turmas', views.turmas, name="adm_turmas"),
        path('administrativo/turmas/criar', views.criar_turmas, name="adm_turmas_criar"),
        path('administrativo/turmas/listar', views.listar_turmas, name="adm_turmas_listar"),
    
    #API
    path('cursos/candidato/<id>', views.candidatar, name="candidatar"),
    path('cursos/<id_curso>/get-candidato/', views.get_candidatos, name="get_candidatos")    
]