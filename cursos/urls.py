from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('cursos/', views.cursos, name="cursos"),        
    
    path('cursos/listar-candidatos/<id>', views.listar_candidatos_curso, name="listar_candidatos_curso"),
    
    # path('cursos/cadastrar-categoria', views.cadastrar_categoria, name="cadastrar_categoria"),
    # path('cursos/cadastrar-local', views.cadastrar_local, name="cadastrar_local"),
    
    path('prematricula/', views.prematricula, name="prematricula"),
    path('alterarCadastro/', views.alterarCad, name="alterarCad"),
    path('resultado/', views.resultado, name="resultado"),
    #ADMINISTRATIVO
    path('administrativo/', views.administrativo, name="administrativo"),
        ##LOCAIS
        path('administrativo/locais/', views.adm_locais, name="adm_locais"),
        path('administrativo/locais/cadastrar', views.adm_locais_criar, name="cadastrar_local"),
        path('administrativo/locais/listar', views.listar_locais, name="adm_locais_listar"),
        path('administrativo/locais/editar/<id>', views.adm_locais_editar, name="adm_locais_editar"),
        ##CATEGORIAS
        path('administrativo/categorias/', views.adm_categorias, name="adm_categorias"),
        path('administrativo/categorias/cadastrar', views.adm_categorias_criar, name="cadastrar_categoria"),
        path('administrativo/categorias/listar', views.listar_categorias, name="adm_categorias_listar"),
        path('administrativo/categorias/editar/<id>', views.adm_categorias_editar, name="adm_categorias_editar"),
        ##CURSOS
        path('administrativo/cursos/', views.adm_cursos, name="adm_cursos"),
        path('administrativo/cursos/cadastrar', views.cadastrar_curso, name="cadastrar_curso"),
        path('administrativo/cursos/listar', views.listar_cursos, name="adm_cursos_listar"),
        path('administrativo/cursos/editar/<id>', views.editar_curso, name="editar_curso"),

        ##Instrutores
        path('administrativo/instrutores/', views.adm_professores, name="adm_professores"),
        path('administrativo/instrutores/criar', views.adm_professores_criar, name="adm_professores_criar"),
        path('administrativo/instrutores/listar', views.adm_professores_listar, name="adm_professores_listar"),        
        path('administrativo/instrutores/editar/<id>', views.adm_professores_editar, name="adm_professores_editar"),
        ##TURMAS
        path('administrativo/turmas', views.turmas, name="adm_turmas"),
        path('administrativo/turmas/criar', views.criar_turmas, name="adm_turmas_criar"),
        path('administrativo/turmas/listar', views.listar_turmas, name="adm_turmas_listar"),        
        path('administrativo/turmas/listar/<id>/visualizar', views.visualizar_turma, name="adm_turma_visualizar"),
        path('administrativo/turmas/listar/<id>/visualizar/editar', views.visualizar_turma_editar, name="adm_turma_visualizar_editar"),
        path('administrativo/turmas/listar/<id>/visualizar/editar/excluir', views.excluir_turma, name="adm_turma_excluir"),
        path('administrativo/turmas/listar/<id>/visualizar/selecionado/<id_selecionado>', views.visualizar_turma_selecionado, name="adm_turma_visualizar_selecionado"),
        ##ALUNOS
        path('administrativo/alunos', views.adm_alunos_listar, name="adm_alunos"),
        path('administrativo/alunos/<id>/visualizar', views.adm_alunos_visualizar, name="adm_alunos_visualizar"),

    #API
    path('cursos/candidato/<id>', views.candidatar, name="candidatar"),
    path('cursos/<id_curso>/get-candidato/', views.get_candidatos, name="get_candidatos"),

    path('login/', views.login_view, name='login'),  
]