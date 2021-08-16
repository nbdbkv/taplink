from django import forms

from apps.customer.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone_number', 'address',
            'payment_method'
        )
        widgets = {'payment_method': forms.RadioSelect()}
