# Generated by Django 2.2 on 2021-05-18 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taplink', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taplink',
            name='url',
        ),
        migrations.AddField(
            model_name='taplink',
            name='nickname',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Nickname'),
        ),
        migrations.AddField(
            model_name='taplinkmessenger',
            name='title_t',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telegram title'),
        ),
        migrations.AddField(
            model_name='taplinkmessenger',
            name='title_wa',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='WhatsApp title'),
        ),
        migrations.AlterField(
            model_name='taplinkeditor',
            name='taplink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editors', to='taplink.TapLink', verbose_name='TapLink'),
        ),
        migrations.AlterField(
            model_name='taplinkmessenger',
            name='taplink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messengers', to='taplink.TapLink', verbose_name='TapLink'),
        ),
    ]
