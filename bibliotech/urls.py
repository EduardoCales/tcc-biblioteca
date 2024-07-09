from django.urls import path

from . import views

app_name = 'livros'


urlpatterns = [
    path('', views.home, name="home"),
    path('livros/<slug:id>/', views.livro, name="livro")
]