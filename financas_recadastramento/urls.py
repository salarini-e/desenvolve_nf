from django.urls import path
from . import views

app_name = 'financas_recadastramento'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkcpf/', views.checkCPF, name='checkCPF'),
    path('checkcpf-2/', views.checkCPF2, name='checkCPF2'),
    path('cadastrar-pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
]