from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from apps.shop.utils import image_upload_to, create_unique_slug
from apps.taplink.models import TapLink


CustomUser = get_user_model()


class Collection(models.Model):
    """Model for creating a Collection object."""
    collection_name = models.CharField(
        max_length=200, unique=True, verbose_name='Collection'
    )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('collection_name',)

    def __str__(self):
        return self.collection_name

    def save(self, *args, **kwargs):
        """Save the current instance with a unique slug."""
        if not self.slug:
            self.slug = create_unique_slug(Collection, self.collection_name)
        return super().save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse('products_by_collection', kwargs={'slug': self.slug})


class Product(models.Model):
    """Model for creating a Product object."""
    product_name = models.CharField(max_length=250, verbose_name='Product')
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(
        null=True, blank=True, verbose_name='Description'
    )
    collection = models.ForeignKey(
        to=Collection, on_delete=models.CASCADE, null=True, blank=True,
        related_name='products', verbose_name='Collections'
    )
    new_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='New price'
    )
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Old price'
    )
    is_available = models.BooleanField(default=True, verbose_name='Available')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Created date'
    )
    seller = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name='products',
        verbose_name='Seller'
    )

    class Meta:
        ordering = ('product_name',)

    def __str__(self):
        return self.product_name

    # def get_absolute_url(self):
    #     return reverse('product-detail_page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Save the current instance with a unique slug."""
        if not self.slug:
            self.slug = create_unique_slug(Product, self.product_name)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    """Model for creating an Image object for Product model."""
    image = models.ImageField(
        upload_to=image_upload_to, blank=True, verbose_name='Image'
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, null=True, blank=True,
        related_name='images', verbose_name='Products'
    )
    is_default = models.BooleanField()

    def __str__(self):
        return self.product.product_name
