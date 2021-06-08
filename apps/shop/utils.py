import os
import hashlib

from django.template.defaultfilters import slugify


def main_image_upload_to(instance, filename):
    basename = os.path.basename(filename)
    root, ext = os.path.splitext(basename)
    hash_object = hashlib.md5(f"{root}".encode())
    return f'shop/{instance.seller.taplinks}/{instance.product_name}/' \
           f'{hash_object.hexdigest()}{ext}'


def image_upload_to(instance, filename):
    basename = os.path.basename(filename)
    root, ext = os.path.splitext(basename)
    hash_object = hashlib.md5(f"{root}".encode())
    return f'shop/{instance.product.seller.taplinks}/{instance.product.product_name}/' \
           f'{hash_object.hexdigest()}{ext}'


def create_unique_slug(klass, field, instance=None):
    """Create unique slug if origin slug exists."""
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug}-{numb}'
        numb += 1
    return unique_slug
