from django.contrib import admin
from django.urls import path
from . import views
 
app_name='cursos'
urlpatterns = [
    path('', views.index, name='home'),
    path('atividade/<tipo>', views.cursos, name="cursos"),            
    path('atividade/<tipo>/<id>/detalhe', views.curso_detalhe, name="curso_detalhe"),            
    path('prematricula/', views.prematricula, name="prematricula"),

]