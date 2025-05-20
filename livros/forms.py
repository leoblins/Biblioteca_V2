from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    url_capa = forms.URLField(
        label='Ou cole o link da capa (opcional)',
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'https://exemplo.com/capa.jpg'})
    )

    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'genero', 'descricao', 'local', 'nota', 'lido', 'capa', 'url_capa', 'preco', 'onde_comprar_nome', 'onde_comprar_link']




