from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.db.models import Q
from django.contrib import messages
import urllib.request
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import os


def home(request):
    termo = request.GET.get('q', '')
    autor_filtro = request.GET.get('autor', '')
    genero_filtro = request.GET.get('genero', '')

    locais = {}
    for local in ['Físico', 'Kindle', 'Play Livros', 'Lista de Desejos']:
        livros = Livro.objects.filter(local=local)

        if termo:
            livros = livros.filter(
                Q(nome__icontains=termo) |
                Q(autor__icontains=termo)
            )

        if autor_filtro:
            livros = livros.filter(autor=autor_filtro)

        if genero_filtro:
            livros = livros.filter(genero=genero_filtro)

        locais[local] = livros

    autores = Livro.objects.values_list('autor', flat=True).distinct().order_by('autor')
    generos = Livro.objects.values_list('genero', flat=True).distinct().order_by('genero')

    context = {
        'locais': locais,
        'termo': termo,
        'autor_filtro': autor_filtro,
        'genero_filtro': genero_filtro,
        'autores': autores,
        'generos': generos,
    }
    return render(request, 'livros/home.html', context)


def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)

            url_capa = form.cleaned_data.get('url_capa')
            if url_capa and not request.FILES.get('capa'):
                livro.capa.save('capa_baixada.jpg', baixar_imagem(url_capa))

            livro.save()
            messages.success(request, 'Livro adicionado com sucesso!')
            return redirect('home')
    else:
        form = LivroForm()
    return render(request, 'livros/adicionar_livro.html', {'form': form})


def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)

    if request.method == 'POST':
        if form.is_valid():
            livro = form.save(commit=False)
            nova_url = form.cleaned_data.get('url_capa')

            if nova_url:
                try:
                    if livro.capa:
                        livro.capa.delete(save=False)

                    img_temp = NamedTemporaryFile()
                    with urllib.request.urlopen(nova_url) as u:
                        img_temp.write(u.read())
                    img_temp.flush()

                    livro.capa.save(os.path.basename(nova_url), File(img_temp), save=False)
                except Exception as e:
                    messages.error(request, f'Erro ao baixar imagem da URL: {e}')

            livro.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect('home')

    return render(request, 'livros/editar_livro.html', {'form': form})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    # Exclui imagem da capa, se existir
    if livro.capa and livro.capa.path:
        if os.path.isfile(livro.capa.path):
            os.remove(livro.capa.path)

    livro.delete()
    messages.success(request, 'Livro excluído com sucesso!')
    return redirect('home')



def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'livros/detalhes_livro.html', {'livro': livro})


# View de registro removida
# def registro(request): ...


def baixar_imagem(url):
    img_temp = NamedTemporaryFile()
    with urllib.request.urlopen(url) as u:
        img_temp.write(u.read())
    img_temp.flush()
    return File(img_temp)
