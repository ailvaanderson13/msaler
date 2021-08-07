from django import forms
from .models import Cliente


class FormCliente(forms.ModelForm):
    nome = forms.CharField(
        label="Nome da Categoriaria",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o nome da categoria'
            }
        )
    )

    sobrenome = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o sobrenome: '
            }
        )
    )

    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o CPF'
            }
        )
    )

    telefone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone'
            }
        )
    )

    email = forms.EmailField(
        label="Nome da Categoriaria",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o nome da categoria'
            }
        )
    )

    model = Cliente
    fields = [
        'nome', 'sobrenome', 'cpf', 'telefone', 'email'
    ]
