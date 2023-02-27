

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cidade-inteligente', views.cidade_inteligente_home, name='cidade_inteligente'),
]
