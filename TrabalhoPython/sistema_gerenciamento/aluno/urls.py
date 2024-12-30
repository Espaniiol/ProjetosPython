from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alunos, name='listar_alunos'),
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
]
