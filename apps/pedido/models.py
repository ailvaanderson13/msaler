from django.db import models
from apps.cliente.models import Cliente
from apps.store.models import Store
from apps.item.models import Item
from apps.employee.models import Employee


class Pedido(models.Model):
    codigo = models.CharField(max_length=15)
    employee = models.ForeignKey(to=Employee, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(to=Cliente, on_delete=models.DO_NOTHING, blank=True, null=True)
    item = models.ManyToManyField(to=Item)
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.cliente.nome}"

    class Mets:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'