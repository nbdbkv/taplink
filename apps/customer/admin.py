from django.contrib import admin

from apps.customer.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'phone_number', 'ordered_at',
        'is_paid', 'payment_method'
    )
    list_filter = ('ordered_at', 'is_paid')
    inlines = [OrderItemInline]
    ordering = ('id',)
