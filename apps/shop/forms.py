from django import forms

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name', 'description', 'old_price', 'current_price', 'quantity',
            'is_available'
        )


class ProductImageForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = ProductImage
        fields = ('image',)
