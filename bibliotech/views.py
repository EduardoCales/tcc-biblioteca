from django.shortcuts import render
from utils.bibliotech.factory import make_book

def home(request):
    return render(request, 'bibliotech/pages/home.html', context= {
        'livros': [make_book() for _ in range(10)],
    })

def livro(request, id):
    return render(request, 'bibliotech/pages/livro-view.html', context={
        'livro': make_book(),
    })
