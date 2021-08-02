from django.db import models

from apps.customer.choices import PAYMENT_CHOICES, CASH
from apps.shop.models import Product
from apps.taplink.models import TapLink


class Order(models.Model):
    """Model for creating an Order object."""
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    address = models.CharField(max_length=250, verbose_name='Address')
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of order')
    is_paid = models.BooleanField(default=False, verbose_name='Order is paid')
    payment_method = models.CharField(
        max_length=100, verbose_name='Payment method', choices=PAYMENT_CHOICES, default=CASH
    )

    class Meta:
        """Order dates of order from last."""
        ordering = ('-ordered_at',)

    def __str__(self):
        """Return order by id."""
        return self.id

    def get_total_cost(self):
        """Count total cost of all items."""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Model for creating an ordered Item object."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    product_owner = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='product_owners', verbose_name='Owner'
    )

    def __str__(self):
        return self.id

    def get_cost(self):
        """Count total cost for product."""
        return self.price * self.quantity
