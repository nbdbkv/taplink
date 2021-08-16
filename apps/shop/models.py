from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from apps.shop.utils import image_upload_to, create_unique_slug
from apps.taplink.models import TapLink


CustomUser = get_user_model()


class Product(models.Model):
    """Model for creating a Product object."""
    name = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание'
    )
    collections = models.ManyToManyField(
        to='Collection', related_name='products', verbose_name='Коллекции'
    )
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Старая цена'
    )
    current_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Новая цена'
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    owner = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='products',
        verbose_name='Владелец'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        """Return product by the name."""
        return self.name

    def save(self, *args, **kwargs):
        """Save the current instance with a unique slug."""
        if not self.slug:
            self.slug = create_unique_slug(Product, self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url_for_owner(self):
        """Return URL for a given object over HTTP."""
        return reverse(
            'product-owner',
            kwargs={
                'shop_owner': self.owner.pathname,
                'product_owner': self.slug
            }
        )

    def get_absolute_url_for_customer(self):
        """Return URL for a given object over HTTP."""
        return reverse(
            'product-customer',
            kwargs={
                'shop_customer': self.owner.pathname,
                'product_customer': self.slug
            }
        )


class Collection(models.Model):
    """Model for creating a Collection object."""
    name = models.CharField(
        max_length=200, unique=True, verbose_name='Название'
    )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        """Return collection by the name."""
        return self.name

    def save(self, *args, **kwargs):
        """Save the current instance with a unique slug."""
        if not self.slug:
            self.slug = create_unique_slug(Collection, self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return URL for a given object over HTTP."""
        return reverse('collection_page', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    """Model for creating an Image object for Product model."""
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение'
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images',
        verbose_name='Товар'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        """Return images by product's name."""
        return self.product.name

    def get_absolute_url(self):
        """Return URL for a given object over HTTP."""
        return reverse('shop-inner', kwargs={'slug': self.product.slug})
