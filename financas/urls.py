from django.urls import path
from . import views

app_name='financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('alvara2dsagdagsjd/', views.alvara, name='alvara'),
    path('alvara/<nome>', views.get_alvara, name='get_alvara'),
    path('certidao',views.certidao, name='certidao'),
    path('certidao/<nome>',views.get_certidao, name='get_certidao'),
]