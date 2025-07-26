from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]
