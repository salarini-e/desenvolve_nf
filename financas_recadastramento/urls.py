from django.urls import path
from . import views

app_name = 'financas_recadastramento'
urlpatterns = [
    path('interno/', views.index, name='index'),
    path('interno/export_to_excel/', views.exportar_cadastro_to_excel, name='export_to_excel'),
    path('cadastral/', views.atualziacao_cadastral, name='atualizacao_cadastral'),
    path('localizar/contribuinte/', views.listar_contribuintes, name='listar_contribuintes'),
    path('checkcpf/', views.checkCPF, name='checkCPF'),
    path('checkcpf-2/', views.checkCPF2, name='checkCPF2'),
    path('interno/cadastrar-pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('interno/cadastrar-processo/', views.cadastrar_processo, name='cadastrar_processo'),
    path('interno/cadastrar-inscricao/', views.cadastrar_inscricao, name='cadastrar_inscricao'),
    path('interno/cadastrar-usuarios/', views.cadastar_usuarios_no_recadastramento, name='cadastrar_usuarios'),
]