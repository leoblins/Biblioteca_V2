from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Opções válidas para o campo "local"
LOCAL_CHOICES = [
    ('Kindle', 'Kindle'),
    ('Play Livros', 'Play Livros'),
    ('Físico', 'Físico'),
]

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    local = models.CharField(max_length=20, choices=LOCAL_CHOICES)

    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    url_capa = models.URLField(blank=True, null=True)



    lido = models.BooleanField(default=False)
    genero = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome

# Exclui a imagem da capa do disco quando o livro for deletado
@receiver(post_delete, sender=Livro)
def excluir_arquivo_capa(sender, instance, **kwargs):
    if instance.capa and instance.capa.path:
        if os.path.isfile(instance.capa.path):
            os.remove(instance.capa.path)
