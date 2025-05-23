from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='livros/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),

    # Recuperação de senha
    path('senha-esquecida/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),

    path('senha-enviada/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('resetar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('resetar-concluido/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
