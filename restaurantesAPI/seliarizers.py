from rest_framework import serializers
from restaurantesAPI.models import Franquia, Pratos

class FranquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franquia
        fields = "__all__"
        
class PratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pratos
        fields = "__all__"
        
