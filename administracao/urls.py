from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.administrativo, name="administrativo"),

    path('instiuicoes', views.adm_instituicoes_listar, name="adm_instituicoes_listar"),
    path('instituicao/cadastrar', views.adm_instituicao_criar, name="adm_cadastrar_instituicao"),
    path('instituicao/<id>', views.adm_locais_editar, name="adm_editar_instituicao"),
    path('instituicao/<id>/excluir', views.adm_locais_excluir, name="adm_locais_excluir"),
    # MISSING EDITAR 

    path('locais', views.adm_locais_listar, name="adm_locais_listar"),
    path('local/cadastrar', views.adm_locais_criar, name="cadastrar_local"),
    path('local/<id>/editar', views.adm_locais_editar, name="adm_locais_editar"),
    path('locai/<id>/excluir', views.adm_locais_excluir, name="adm_locais_excluir"),
    # MISSING VISUALIZAR

    path('categorias', views.adm_categorias_listar, name="adm_categorias_listar"),
    path('categoria/cadastrar', views.adm_categorias_criar, name="cadastrar_categoria"),
    path('categoria/<id>/editar', views.adm_categorias_editar, name="adm_categorias_editar"),
    path('categoria/<id>/excluir', views.adm_categorias_excluir, name="adm_categorias_excluir"),
    # MISSING VISUALIZAR

    path('cursos', views.adm_cursos_listar, name="adm_cursos_listar"),
    path('curso/cadastrar', views.adm_cursos_criar, name="adm_cursos_criar"),
    path('curso/<id>/editar', views.adm_cursos_editar, name="adm_cursos_editar"),
    # MISSING VISUALIZAR e EXCLUIR

    path('instrutores', views.adm_professores_listar, name="adm_professores_listar"),        
    path('instrutor/criar', views.adm_professores_criar, name="adm_professores_criar"),
    path('instrutor/<id>/editar', views.adm_professores_editar, name="adm_professores_editar"),
    path('instrutor/<id>/excluir', views.adm_professores_excluir, name="adm_professores_excluir"),
    # MISSING VISUALIZAR

    path('turmas', views.adm_turmas_listar, name="adm_turmas_listar"),
    path('turma/criar', views.adm_turmas_criar, name="adm_turmas_criar"),
    path('turma/<id>', views.adm_turmas_visualizar, name="adm_turma_visualizar"),
    path('turma/<id>/editar', views.visualizar_turma_editar, name="adm_turma_editar"),
    path('turma/<id>/excluir', views.excluir_turma, name="adm_turma_excluir"),

    path('turma/<id>/turno/criar', views.adm_turno_criar, name="adm_turno_criar"),
    # MISSING VISUALIZAR, EDITAR, LISTAR E EXCLUIR

    path('turma/<turma_id>/aula/criar', views.adm_aula_criar, name="adm_aula_criar"),
    path('turma/<turma_id>/aulas', views.adm_aulas_listar, name="adm_aulas_listar"),
    path('turma/<turma_id>/aula/<aula_id>', views.adm_aula_visualizar, name="adm_aula_visualizar"),
    # MISSING EDITAR E EXCLUIR

    # -------- Serve para confirmar um aluno selecionado, transformando seu status para "Aluno" -------- #
    path('turma/selecionado/<matricula>', views.visualizar_turma_selecionado, name="adm_turma_visualizar_selecionado"),
    # -------- # -------- #
    
    path('justificativa/<presenca_id>/criar', views.adm_justificativa_criar, name="adm_justificativa_criar"),
    path('justificativa/<presenca_id>', views.adm_justificativa_visualizar, name="adm_justificativa_visualizar"),
    # MISSING LISTAR, EDITAR E EXCLUIR

    path('aluno', views.adm_alunos_listar, name="adm_alunos_listar"),
    path('aluno/<id>', views.adm_aluno_visualizar, name="adm_aluno_visualizar"),
    path('aluno/<id>/editar', views.adm_aluno_editar, name="adm_aluno_editar"),
    path('aluno/<matricula>/desmatricular', views.desmatricular_aluno, name="adm_desmatricular_aluno"),

]