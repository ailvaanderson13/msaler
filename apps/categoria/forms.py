from django import forms
from .models import Category


class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome da Categoriaria",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o nome da categoria'
            }
        )
    )

    descricao = forms.CharField(
        label="Descrição",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira uma descrição'
            }
        )
    )

    model = Category
    fields = [
        'nome', 'descricao'
    ]