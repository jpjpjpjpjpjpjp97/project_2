from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewset(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer