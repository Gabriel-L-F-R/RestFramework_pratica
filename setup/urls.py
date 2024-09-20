from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurantesAPI.views import PratosViewSet, FranquiaViewSet, RestauranteViewSet

router = routers.DefaultRouter()

router.register('pratos',PratosViewSet, basename= "Pratos" )
router.register('franquia',FranquiaViewSet, basename= "Franquia" )
router.register('restaurante',RestauranteViewSet, basename= "Restaurante" )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
