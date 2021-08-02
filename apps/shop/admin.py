from django.contrib import admin

from .models import Collection, Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'old_price', 'current_price', 'quantity', 'is_available', 'created', 'owner'
    )


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
