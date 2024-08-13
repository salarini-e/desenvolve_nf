from django.urls import path
from . import views
 
app_name='forms'
urlpatterns = [
    
    path('PCA/', views.lista_cadastros_pca, name='lista_cadastros_pca'),
    path('PCA/novo/', views.criar_cadastro_pca, name='criar_cadastro_pca'),
    path('PCA/<int:pk>/editar/', views.editar_cadastro_pca, name='editar_cadastro_pca'),
    path('sala-do-emprendedor/empresarios/', views.BackupDatabaseView.as_view(), name='backup_database'),
]