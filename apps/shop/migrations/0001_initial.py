# Generated by Django 2.2 on 2021-06-23 05:47

import apps.shop.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taplink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Collection')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Product')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Old price')),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Current price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('is_available', models.BooleanField(default=True, verbose_name='Available')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('collections', models.ManyToManyField(related_name='products', to='shop.Collection', verbose_name='Collections')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='taplink.TapLink', verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=apps.shop.utils.image_upload_to, verbose_name='Image')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Product', verbose_name='Products')),
            ],
        ),
    ]
