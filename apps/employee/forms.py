from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    loja = forms.ModelChoiceField(
        label="Selecione a loja",
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    model = Employee
    exclude = ['is_active', 'is_staff', 'date_joined']
    fields = "__all__"
