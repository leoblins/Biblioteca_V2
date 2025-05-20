from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'genero', 'descricao', 'local', 'nota', 'lido', 'capa', 'preco', 'onde_comprar_nome', 'onde_comprar_link']




