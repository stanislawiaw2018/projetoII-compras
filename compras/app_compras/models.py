from django.db import models

# Create your models here.
class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    unidades = models.IntegerField()
    quant_mes = models.FloatField(round(2))
    preco = models.FloatField(round(2))
    preco_max = models.FloatField(round(2))

    def __str__(self):
        return self.nome

