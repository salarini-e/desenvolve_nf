from django.urls import path
from . import views
 
app_name='empreendedor'
urlpatterns = [
    path('', views.index, name='index'),
    path('consultar-protocolo', views.consultar_protocolo, name='consultar_protocolo'),
    path('faccao-legal', views.faccao_legal, name='faccao_legal'),
    path('vitrine-virtual', views.vitrine_virtual, name='vitrine_virtual'),
    path('quero-ser-mei', views.quero_ser_mei, name='quero_ser_mei'),
    path('ja-sou-mei', views.ja_sou_mei, name='ja_sou_mei'),
    path('abertuda-de-empresa', views.abertura_de_empresa, name='abertura_de_empresa'),
]