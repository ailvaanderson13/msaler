from django.db import models


class Store(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
