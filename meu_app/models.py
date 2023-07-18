from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome
    
class TesteBd(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome