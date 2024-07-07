from django.urls import path

from bibliotech.views import home, sobre, contato


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]