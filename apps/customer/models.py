from django.db import models

from apps.customer.choices import PAYMENT_CHOICES, CASH
from apps.shop.models import Product
from apps.taplink.models import TapLink


class Order(models.Model):
    """Model for creating an Order object."""
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone_number = models.CharField(
        max_length=20, verbose_name='Мобильный номер'
    )
    address = models.CharField(max_length=250, verbose_name='Адрес покупателя')
    ordered_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата заказа'
    )
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    payment_method = models.CharField(
        max_length=100, choices=PAYMENT_CHOICES, default=CASH,
        verbose_name='Способы оплаты'
    )

    class Meta:
        """Order dates of order from last."""
        ordering = ('-ordered_at',)
        verbose_name = 'Данные покупателя'
        verbose_name_plural = 'Данные покупателя'

    def __str__(self):
        """Return order by id."""
        return f'Заказ {self.id}'

    def get_total_cost(self):
        """Count total cost of all items."""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Model for creating an ordered Item object."""
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, related_name='items',
        verbose_name='Заказы'
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE,  related_name='order_items',
        verbose_name='Товары'
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    product_owner = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='product_owners',
        verbose_name='Владелец товара'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        """Count total cost for product."""
        return self.price * self.quantity
