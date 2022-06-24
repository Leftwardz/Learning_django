from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True)
    img = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

