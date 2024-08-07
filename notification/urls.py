from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    path('/<hash>/', views.view_notification, name='visualizar'),
]