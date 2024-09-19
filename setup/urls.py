from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurantesAPI.views import PratosViewSet, FranquiaViewSet

router = routers.DefaultRouter()

router.register('pratos',PratosViewSet, basename= "Pratos" )
router.register('franquia',FranquiaViewSet, basename= "Franquia" )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
