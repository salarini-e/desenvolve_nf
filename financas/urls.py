from django.urls import path
from . import views

app_name = 'financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('formularios', views.formularios, name='formularios'),
]
