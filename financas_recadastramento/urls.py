from django.urls import path
from . import views

app_name = 'financas_recadastramento'
urlpatterns = [
    path('interno/', views.index, name='index'),
    path('cadastral/', views.atualziacao_cadastral, name='atualizacao_cadastral'),
    path('localizar/contribuinte/', views.listar_contribuintes, name='listar_contribuintes'),
    path('checkcpf/', views.checkCPF, name='checkCPF'),
    path('checkcpf-2/', views.checkCPF2, name='checkCPF2'),
    path('cadastrar-pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('cadastrar-processo/', views.cadastrar_processo, name='cadastrar_processo'),
    path('cadastrar-inscricao/', views.cadastrar_inscricao, name='cadastrar_inscricao'),
    path('cadastrar-usuarios/', views.cadastar_usuarios_no_recadastramento, name='cadastrar_usuarios'),
]