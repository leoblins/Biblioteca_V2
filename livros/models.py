from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
import os

# Opções de categorias para o carrossel
LOCAL_CHOICES = [
    ('Kindle', 'Kindle'),
    ('Play Livros', 'Play Livros'),
    ('Físico', 'Físico'),
    ('Lista de Desejos', 'Lista de Desejos'),
]

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    local = models.CharField(max_length=20, choices=LOCAL_CHOICES)  # ✅ novo campo
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    nota = models.DecimalField(
    max_digits=3,
    decimal_places=1,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ],
    blank=True,
    null=True
)
    lido = models.BooleanField(default=False) 
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    onde_comprar = models.CharField(max_length=255, blank=True, null=True)


    onde_comprar_nome = models.CharField(max_length=100, blank=True, null=True)
    onde_comprar_link = models.URLField(blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    



    def __str__(self):
        return self.nome

@receiver(post_delete, sender=Livro)
def excluir_arquivo_capa(sender, instance, **kwargs):
    if instance.capa:
        if os.path.isfile(instance.capa.path):
            os.remove(instance.capa.path)       
