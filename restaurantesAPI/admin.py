from django.contrib import admin
from restaurantesAPI.models import Pratos, Franquia

class Prato(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ("nome",)

    
admin.site.register(Pratos, Prato)

class Franquias(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ("nome",)

    
admin.site.register(Franquia, Franquias)