from django.shortcuts import render

def home(request):
    return render(request, 'bibliotech/pages/home.html')
