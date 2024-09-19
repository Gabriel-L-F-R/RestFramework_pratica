from rest_framework import viewsets
from restaurantesAPI.models import Franquia, Pratos
from restaurantesAPI.seliarizers import FranquiaSerializer, PratosSerializer

class PratosViewSet(viewsets.ModelViewSet):
    
    queryset = Pratos.objects.all()
    serializer_class = PratosSerializer
    
class FranquiaViewSet(viewsets.ModelViewSet):
    
    queryset = Franquia.objects.all()
    serializer_class = FranquiaSerializer


