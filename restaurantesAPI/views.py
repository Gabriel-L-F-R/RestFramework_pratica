from rest_framework import viewsets
from restaurantesAPI.models import Franquia, Pratos, Restaurante
from restaurantesAPI.seliarizers import FranquiaSerializer, PratosSerializer,RestauranteSerializer

class PratosViewSet(viewsets.ModelViewSet):
    
    queryset = Pratos.objects.all()
    serializer_class = PratosSerializer
    
class FranquiaViewSet(viewsets.ModelViewSet):
    
    queryset = Franquia.objects.all()
    serializer_class = FranquiaSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
