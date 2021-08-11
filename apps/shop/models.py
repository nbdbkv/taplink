from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from apps.shop.utils import image_upload_to, create_unique_slug
from apps.taplink.models import TapLink


CustomUser = get_user_model()


class Product(models.Model):
    """Model for creating a Product object."""
    name = models.CharField(max_length=120, verbose_name='Product')
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    collections = models.ManyToManyField(to='Collection', related_name='products', verbose_name='Collections')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Old price')
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Current price')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    is_available = models.BooleanField(default=True, verbose_name='Available')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    owner = models.ForeignKey(to=TapLink, on_delete=models.CASCADE, related_name='products', verbose_name='Owner')

    def __str__(self):
        """Return product by the name."""
        return self.name

    def get_absolute_url_for_owner(self):
        """Return URL for a given object over HTTP."""
        return reverse('product-owner', kwargs={'shop_owner': self.owner.pathname, 'product_owner': self.slug})

    def get_absolute_url_for_customer(self):
        """Return URL for a given object over HTTP."""
        return reverse(
            'product-customer', kwargs={'shop_customer': self.owner.pathname, 'product_customer': self.slug}
        )

    def save(self, *args, **kwargs):
        """Save the current instance with a unique slug."""
        if not self.slug:
            self.slug = create_unique_slug(Product, self.name)
        return super().save(*args, **kwargs)


class Collection(models.Model):
    """Model for creating a Collection object."""
    name = models.CharField(max_length=200, unique=True, verbose_name='Collection')
    slug = models.SlugField(max_length=200, unique=True)

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
    image = models.ImageField(upload_to=image_upload_to, blank=True, verbose_name='Image')
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, null=True, blank=True, related_name='images', verbose_name='Products'
    )

    def __str__(self):
        """Return images by product's name."""
        return self.product.name

    def get_absolute_url(self):
        """Return URL for a given object over HTTP."""
        return reverse('shop-inner', kwargs={'slug': self.product.slug})
