from django import forms

from .models import Collection, Product, ProductImage


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ('collection_name',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'product_name', 'description', 'collection', 'new_price',
            'old_price', 'is_available', 'quantity', 'main_image'
        )


class ProductImageForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = ProductImage
        fields = ('image',)
