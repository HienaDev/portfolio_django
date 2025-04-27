# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'portfolio'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('projeto/<int:pk>/', views.projeto_detalhe, name='projeto_detalhe'),
    path('aluno/<int:aluno_id>/', views.aluno_detalhe, name='aluno_detalhe'),
    path('docente/<int:docente_id>/', views.docente_detalhe, name='docente_detalhe'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_detalhe, name='disciplina_detalhe'),
    path('tecnologia/<int:tecnologia_id>/', views.tecnologia_detalhe, name='tecnologia_detalhe'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
    path('cv/', views.cv_view, name='cv'),
]