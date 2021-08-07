from django import forms
from .models import Item
from apps.categoria.models import Category


class ItemForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        label='Categoria',
        queryset=Category,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira um nome: '
            }
        )
    )

    descricao = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira uma descrição: '
            }
        )
    )

    model = Item
    fields = [
        'categoria', 'nome', 'descricao'
    ]
