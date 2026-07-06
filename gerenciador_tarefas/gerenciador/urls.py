from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('base/', views.base, name='base'),
    path('inicio/', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),

]