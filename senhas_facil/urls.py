from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.posicao_na_fila),
     path('fetch-posicao-na-fila/', views.fetch_posicao_na_fila, name='fetch_posicao_na_fila'),
]