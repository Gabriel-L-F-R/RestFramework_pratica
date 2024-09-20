from rest_framework import serializers
from restaurantesAPI.models import Franquia, Pratos, Restaurante

class FranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franquia
        fields = "__all__"
        
class PratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pratos
        fields = "__all__"

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante 
        fields = "__all__"
