from django.urls import path
from . import views

app_name='almoxarifado'
urlpatterns = [
    path('', views.index, name="index"),
    
    path('listar-tipo-materiais', views.listar_tipo_materiais, name="alm_listar_tipos"),
    path('listar-materiais', views.listar_materiais, name="alm_listar_materiais"),
    path('adicionar-tipo-materiais', views.adicionar_tipo_materiais, name="alm_adicionar_tipo"),
    path('adicionar-material/<tipo>', views.adicionar_material, name="alm_adicionar_material"),
    path('adicionar-material-ao-estoque', views.adicionar_material_ao_estoque, name="alm_adicionar_material_ao_estoque"),
    
]