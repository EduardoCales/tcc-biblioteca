from django.shortcuts import render
from utils.bibliotech.factory import make_book
from bibliotech.models import Livro

def home(request):
    livros = Livro.objects.all().order_by('-id')
    return render(request, 'bibliotech/pages/home.html', context= {
        'livros': livros,
    })

def category(request, category_id):
    livros = Livro.objects.filter(
        category__id=category_id
        ).order_by('-id')
    return render(request, 'bibliotech/pages/home.html', context= {
        'livros': livros,
    })

def livro(request, id):
    return render(request, 'bibliotech/pages/livro-view.html', context={
        'livro': make_book(),
        'is_detail_page': True,
    })
