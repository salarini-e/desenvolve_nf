from django.urls import path
from . import views

app_name = 'financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('formularios/', views.formularios, name='formularios'),
    path('legislacao/', views.legislacao, name='legislacao'),
    path('admin/', views.administracao, name='admin'),
    path('add_conselheiro/', views.add_conselheiro, name='add_conselheiro'),
    path('add_pauta/', views.add_pauta, name='add_pauta'),
    path('add_sumula/', views.add_sumula, name='add_sumula'),
    path('add_acordao/', views.add_acordao, name='add_acordao'),
    path('add_ata/', views.add_ata, name='add_ata'),
    path('add_voto/', views.add_voto_relator, name='add_voto'),
    path('conselho/', views.conselho, name='conselho'),

]
