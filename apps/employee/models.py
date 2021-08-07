from django.contrib.auth.models import AbstractUser
from apps.store.models import Store
from django.db import models


class Employee(AbstractUser):
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.email}"

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionários'
