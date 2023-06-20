from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

app_name='autenticacao'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('passwd_reset/', views.passwd_reset, name='passwd_reset'),

    path('cadastro/', views.cadastro_user, name='cadastrar_usuario'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastrar_aluno'),


]