from django import forms
from .models import Pedido
from apps.cliente.models import Cliente
from apps.item.models import Item


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    item = forms.ModelChoiceField(
        label='Selecione os itens',
        queryset=Item,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    model = Pedido
    forms = [
        'cliente', 'item'
    ]

