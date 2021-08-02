# Generated by Django 2.2 on 2021-07-22 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taplink', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('ordered_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of order')),
                ('is_ordered', models.BooleanField(default=False, verbose_name='Ordered')),
                ('paid_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of payment')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('payment_method', models.CharField(choices=[('НАЛИЧНЫМИ', 'Наличными'), ('ОНЛАЙН ОПЛАТА', 'Онлайн оплата')], max_length=100, verbose_name='Payment method')),
            ],
            options={
                'ordering': ('-ordered_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='customer.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
                ('product_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_owners', to='taplink.TapLink', verbose_name='Owner')),
            ],
        ),
    ]
