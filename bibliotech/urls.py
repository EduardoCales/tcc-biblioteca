from django.urls import path

from bibliotech.views import home


urlpatterns = [
    path('', home),
]