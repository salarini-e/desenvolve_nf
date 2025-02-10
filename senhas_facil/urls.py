from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.posicao_na_fila),
    path('<senha>/', views.posicao_na_fila_2),
    path('<senha>/totem-financas/', views.posicao_na_fila_financas),
    path('fetch-posicao-na-fila/<senha>/totem-empreendedor/', views.fetch_posicao_na_fila, name='fetch_posicao_na_fila'),
    path('fetch-posicao-na-fila/<senha>/totem-financas/', views.fetch_posicao_na_fila_financas, name='fetch_posicao_na_fila'),
]