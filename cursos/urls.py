from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('cursos/', views.cursos, name="cursos"),        
    path('prematricula/', views.prematricula, name="prematricula"),

    #API
    path('login/', views.login_view, name='login'),  
]