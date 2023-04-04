from django.urls import path
from . import views

app_name = 'financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('formularios/<arg>', views.formularios, name='formularios'),
    path('alvara/<arg>', views.alvara, name='alvara'),
    path('certidao/<arg>', views.certidao, name='certidao'),
    path('iptu/<arg>', views.iptu, name='iptu'),
    path('itbi/<arg>', views.itbi, name='itbi'),
    path("isencao/<arg>", views.isencao, name="isencao"),
    path('diversos/<arg>', views.diversos, name='diversos'),
]
