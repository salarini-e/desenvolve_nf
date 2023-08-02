from django.urls import path
from . import views
 
app_name='empreendedor'
urlpatterns = [
    path('', views.index, name='index'),
    path('quero-ser-mei', views.quero_ser_mei, name='quero_ser_mei'),
]