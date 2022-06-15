from threading import Thread
from threading import Lock
from datetime import datetime
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Pokemon
from .serializers import PokemonSerializer

def write_to_file(lock, request):
    lock.acquire()
    my_file = open("api_request_login.txt", "a")
    my_file.write(f'{datetime.utcnow()} | {request.method} | {request.path}\n')
    my_file.close()
    lock.release()

class PokemonViewset(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    def dispatch(self, request, *args, **kwargs):
        lock = Lock()
        Thread(target=write_to_file, args=(lock, request,)).start()
        return super().dispatch(request, *args, **kwargs)