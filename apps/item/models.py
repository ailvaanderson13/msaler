from django.db import models
from apps.categoria.models import Category
from apps.store.models import Store


class Item(models.Model):
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200)
    preco = models.FloatField(max_length=10, blank=True, null=True)
    descricao = models.TextField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'