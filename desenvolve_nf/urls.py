from django.urls import path
from . import views

from django.conf.urls import handler500

handler500 = 'desenvolve_nf.views.error_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('solicitar/newsletter/', views.solicitarNewsLetter, name='newsletter'),
    path('get-clima-tempo/', views.getClimaTempo, name='getClimaTempo'),
    path('cidade-inteligente/', views.cidade_inteligente_home, name='cidade_inteligente'),
    path('cidade-inteligente/cadastro-camera/', views.cidade_inteligente_cadastro_camera, name='cidade_inteligente_cadastro_camera'),
    path('carnaval/', views.carnaval, name='carnaval')
]
