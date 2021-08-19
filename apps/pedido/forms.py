from django import forms
from .models import Pedido
from apps.cliente.models import Cliente
from apps.item.models import Item


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Cliente.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    item = forms.ModelMultipleChoiceField(
        label='Selecione os Produtos',
        queryset=Item.objects.filter(is_active=True),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            }
        )
    )

    obs = forms.CharField(
        label='Observações',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Opcional'
            }
        )
    )

    class Meta:
        model = Pedido
        fields = [
            'cliente', 'item', 'obs'
        ]
