from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    url_capa = forms.URLField(
        label='Cole o link da capa',
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'https://exemplo.com/capa.jpg'})
    )

    class Meta:
        model = Livro
        fields = [
            'nome',
            'autor',
            'genero',
            'local',
            'lido',
            'url_capa',
            'capa',
        ]
