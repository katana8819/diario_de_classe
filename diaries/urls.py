from django.urls import path
from . import views

app_name='diaries'

urlpatterns=[
    #home page
    path('', views.index, name='index'),
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/<int:aluno_id>/', views.aluno, name='aluno'),
    path('inativos/', views.inativo, name='inativo'),
    path('anotacoes/', views.anotacoes, name='anotacoes'),
    path('anotacoes/<int:note_id>/', views.anotacao, name='anotacao'),
    #formulários
    path('novo_aluno/', views.novo_aluno, name='novo_aluno'),
    path('add_anotacao/', views.add_anotacao, name='add_anotacao'),
    path('edit_aluno/<int:aluno_id>/', views.edit_aluno, name='edit_aluno'),
    path('edit_anotacao/<int:note_id>/' , views.edit_anotacao, name='edit_anotacao'),
    #delete
    path('_delete/<int:aluno_id>/', views.del_aluno, name='del_aluno'),
    path('note_delete/<int:note_id>/', views.note_delete, name='note_delete'),
    #busca
    path('results/', views.search, name='search'),
    path('note_results/', views.search_note, name='search_note'),
]
