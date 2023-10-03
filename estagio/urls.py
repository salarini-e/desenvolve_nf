from django.contrib import admin
from django.urls import path

from . import views

app_name = 'estagio'
urlpatterns = [
    path('', views.index, name= 'index'),
    # path('vagas/', views.vagas, name='vagas'),
    path('vagas/', views.listar_instituicoes, name='vagas'),
    path('vagas/<id>/', views.listar_cursos_e_locais, name='listar_cursos_e_locais'),
    
    path('getLocais/<id>/', views.getLocais, name='get_locais'),
    path('getVagas/<id>/', views.getVagas, name='get_vagas'),
    path('getCursos/<id>/', views.getCursos, name='get_cursos'),
    
    path('area-do-estudante/', views.area_do_estudante, name='area_do_estudante'),
    path('area-da-universidade/', views.area_da_universidade, name='area_da_universidade'),
    path('area-do-estudante/processo/156f165f1<id>4f654f', views.processo_da_vaga, name='processo_da_vaga'),
    path('area-do-estudante/processo/156f165f1<id>4f654f/anexar-tce/', views.anexar_tce, name='anexar_tce'),
    path('area-do-estudante/processo/156f165f1<id>4f654f/vizualiar-tce/', views.visualizar_tce, name='visualizar_tce'),
    
    path('adm/', views.adm, name='adm'),
    path('vagas/cadastrar/', views.cadastro_vaga, name='cadastro_vaga'),
    path('vagas/<id>/<id_curso>/canditar-se/', views.candidatar_se_vaga, name='candidatar_se_vaga'),
    path('candidato/', views.listar_candidato, name='candidato'),
    path('estagiario/', views.listar_estagiario, name='estagiario'),
    path('adm/processo/156f165f1<id>4f654f/', views.adm_processo_da_vaga, name='adm_processo_da_vaga'),
    path('candidato/<id>/editar/', views.editar_estudante, name='editar_candidato'),
    path('candidato/<id>/editar/gerar-processo', views.editar_estudante_processo, name='editar_candidato_processo'),
    path('universidade/', views.listar_universidade, name='listar_universidade'),
    path('universidade/cadastrar_universidade/', views.cadastrar_universidade, name="cadastrar_universidade"),
    path('universidade/<id>/cadastrar_curso', views.cadastrar_curso, name='cadastrar_curso'),
    path('universidade/<id>/curso', views.listar_curso, name='curso'),
    path('universidade/<id>/editar', views.editar_curso, name='editar_curso'),
    path('supervisor/', views.listar_supervisor, name='listar_supervisor'),
    path('supervisor/cadastrar_supervisor', views.cadastrar_supervisor, name='cadastrar_supervisor'),
    path('supervisor/<id>/editar', views.editar_supervisor, name='editar_supervisor'),
    path('secretaria/', views.listar_secretaria, name='listar_secretaria'),
    path('secretaria/<id>/locais/', views.listar_secretaria_locais, name='listar_secretaria_locais'),
    path('secretaria/cadastrar_secretaria', views.cadastrar_secretaria, name='cadastrar_secretaria'),
    path('secretaria/<id>/cadastrar_local', views.cadastrar_local, name='cadastrar_local'),
    path('secretaria/<id>/locais/detalhes/<id_local>', views.locais_detalhes, name="listar_detalhes_do_local"),
    path('secretaria/<id>/locais/detalhes/<id_local>/adicionar-ou-remover', views.locais_detalhes_adicionar_ou_remover, name="listar_detalhes_do_local_add_ou_rmv"),    
    path('adm/vagas/', views.listar_vagas, name='listar_vagas'),
    path('adm/vagas/cadastrar', views.cadastrar_vagas, name='cadastrar_vagas'),
    path('adm/vagas/<id>/editar', views.editar_vagas, name='editar_vagas'),
    path('get_courses_by_university/<university_id>', views.get_courses_by_university, name='get_courses_by_university'),

]
