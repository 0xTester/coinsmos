from django.db import models

class Crypto(models.Model):

    cryptocurrency = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    marketcap = models.IntegerField()
    volumen = models.CharField(max_length=200)
    supply = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    imagen = models.CharField(max_length=600, default='https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579')


    class Meta:
        ordering = ['-marketcap']
    def __str__(self):
        return self.cryptocurrency
