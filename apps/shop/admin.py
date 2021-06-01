from django.contrib import admin

from .models import Collection, Product, ProductImage


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collection_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'description', 'collection', 'new_price', 'old_price',
        'quantity', 'is_available', 'created', 'seller'
    )
