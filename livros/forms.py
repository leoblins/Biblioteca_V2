from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    url_capa = forms.URLField(
        label='Cole o link da capa',
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'https://exemplo.com/capa.jpg'})
    )

    descricao = forms.CharField(
        label='Minha crítica',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva sua opinião sobre o livro...'})
    )

    class Meta:
        model = Livro
        fields = [
            'nome', 'autor', 'genero', 'descricao', 'local',
            'nota', 'lido', 'url_capa', 'preco',
            'onde_comprar_nome', 'onde_comprar_link'
        ]
