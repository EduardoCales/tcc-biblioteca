from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'bibliotech/home.html')

def sobre(request):
    return HttpResponse('Sobre1')

def contato(request):
    return HttpResponse('Contato1')