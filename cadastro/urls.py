from django.urls import path
from . import views, api

urlpatterns = [
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('produtos/novo/', views.produto_new, name='produto_new'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('api/usuarios/', api.usuarios, name='api_usuarios'),
]