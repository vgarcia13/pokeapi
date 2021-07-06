from django.contrib import admin
from django.urls import path

from .views import PokeApiViewSet

urlpatterns = [
    path('pokemons/', PokeApiViewSet.as_view({'get': 'list'})),
]
