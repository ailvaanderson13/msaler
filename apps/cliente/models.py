from django.db import models
from apps.store.models import Store


class Cliente(models.Model):
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
