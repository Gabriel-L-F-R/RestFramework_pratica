from django.db import models

class Franquia(models.Model):
    nome = models.CharField(max_length=20, blank=False, null= False)
    descricao = models.CharField(max_length=200)
    endereco = models.CharField(max_length=25, blank=False, null= False)
    
    def __str__(self):
        return self.nome
    
class Pratos(models.Model):
    CATEGORIAS = (
        ("M", "Massas"),
        ("A", "Asiática"),
        ("C", "Carnes"),
        ("V", "Vegetariano"),
        ("F", "Frutos do Mar")
    )
    
    nome = models.CharField(max_length=20, blank=False, null= False)
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=1, choices= CATEGORIAS, default="V", blank=False, null= False)
    
    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=20, blank=False, null= False)
    descricao = models.CharField(max_length=200)
    franquia = models.ForeignKey(Franquia, on_delete=models.CASCADE)
    pratos = models.ForeignKey(Pratos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome