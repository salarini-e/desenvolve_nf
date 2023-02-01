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

    #ADMINISTRATIVO
    path('administrativo/', views.administrativo, name="administrativo"),

        ##LOCAIS
        path('administrativo/locais/', views.adm_locais, name="adm_locais"),
        path('administrativo/locais/cadastrar', views.adm_locais_criar, name="cadastrar_local"),
        path('administrativo/locais/listar', views.adm_locais_listar, name="adm_locais_listar"),
        path('administrativo/locais/editar/<id>', views.adm_locais_editar, name="adm_locais_editar"),
        path('administrativo/locais/excluir/<id>', views.adm_locais_excluir, name="adm_locais_excluir"),

        ##CATEGORIAS
        path('administrativo/categorias/', views.adm_categorias, name="adm_categorias"),
        path('administrativo/categorias/cadastrar', views.adm_categorias_criar, name="cadastrar_categoria"),
        path('administrativo/categorias/listar', views.adm_categorias_listar, name="adm_categorias_listar"),
        path('administrativo/categorias/editar/<id>', views.adm_categorias_editar, name="adm_categorias_editar"),
        path('administrativo/categorias/excluir/<id>', views.adm_categorias_excluir, name="adm_categorias_excluir"),

        ##CURSOS
        path('administrativo/cursos/', views.adm_cursos, name="adm_cursos"),
        path('administrativo/cursos/cadastrar', views.adm_cursos_criar, name="adm_cursos_criar"),
        path('administrativo/cursos/listar', views.adm_cursos_listar, name="adm_cursos_listar"),
        path('administrativo/cursos/editar/<id>', views.adm_cursos_editar, name="adm_cursos_editar"),
        # path('administrativo/cursos/excluir/<id>', views.adm_cursos_excluir, name="adm_cursos_excluir"),


        ##Instrutores
        path('administrativo/instrutores/', views.adm_professores, name="adm_professores"),
        path('administrativo/instrutores/criar', views.adm_professores_criar, name="adm_professores_criar"),
        path('administrativo/instrutores/listar', views.adm_professores_listar, name="adm_professores_listar"),        
        path('administrativo/instrutores/editar/<id>', views.adm_professores_editar, name="adm_professores_editar"),
        path('administrativo/instrutores/excluir/<id>', views.adm_professores_excluir, name="adm_professores_excluir"),

        ##TURMAS
        path('administrativo/turmas', views.turmas, name="adm_turmas"),
        path('administrativo/turmas/criar', views.adm_turmas_criar, name="adm_turmas_criar"),
        path('administrativo/turmas/listar', views.adm_turmas_listar, name="adm_turmas_listar"),        
        path('administrativo/turma/<id>', views.adm_turmas_visualizar, name="adm_turma_visualizar"),
        path('administrativo/turma/<id>/editar', views.visualizar_turma_editar, name="adm_turma_editar"),
        path('administrativo/turma/<id>/excluir', views.excluir_turma, name="adm_turma_excluir"),

        path('administrativo/turma/selecionado/<matricula>', views.visualizar_turma_selecionado, name="adm_turma_visualizar_selecionado"),
        path('administrativo/aluno/<matricula>/desmatricular', views.desmatricular_aluno, name="adm_desmatricular_aluno"),
        
        ##ALUNOS
        path('administrativo/alunos/listar', views.adm_alunos_listar, name="adm_alunos_listar"),
        path('administrativo/aluno/<id>', views.adm_aluno_visualizar, name="adm_aluno_visualizar"),
        path('administrativo/aluno/<id>/editar', views.adm_aluno_editar, name="adm_aluno_editar"),
        path('administrativo/aluno/<id>/excluir', views.adm_aluno_excluir, name="adm_aluno_excluir"),
        # path('administrativo/turma/<id_turma>/aluno/<id_aluno>/desmatricular', views.desmatricular_aluno, name="adm_turma_desmatricular_aluno"),

    #API
    path('cursos/candidato/<id>', views.candidatar, name="candidatar"),
    path('cursos/<id_curso>/get-candidato/', views.get_candidatos, name="get_candidatos"),
    path('turmas/autenticar_data', views.autenticar_data_candidato, name="autenticar_data_candidato"),
    path('login/', views.login_view, name='login'),  
    path('testar/email', views.testar_email)
]