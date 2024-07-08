from django.shortcuts import render

def home(request):
    return render(request, 'bibliotech/pages/home.html')

def livro(request, id):
    return render(request, 'bibliotech/pages/home.html')
