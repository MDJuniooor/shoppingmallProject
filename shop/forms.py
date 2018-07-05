from django import forms
from .models import order

class OrderForm(forms.ModelForm):
    class Meta:
        model= order
        fields = ('name', 'amount')
        widgets = {
            'name': forms.TextInput(attrs={'readonly':'readonly'}),
            'amount': forms.TextInput(attrs={'readonly':'readonly'})
        }