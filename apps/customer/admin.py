from django.contrib import admin

from apps.customer.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('ordered_at', 'is_paid')
    list_display_links = ('first_name', 'last_name')
    inlines = [OrderItemInline]
