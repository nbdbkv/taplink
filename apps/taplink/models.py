from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from apps.taplink.utils import image_upload_to


CustomUser = get_user_model()


class TapLink(models.Model):
    pathname = models.SlugField(
        max_length=50, unique=True, null=True, blank=True, verbose_name='Путь'
    )
    avatar = models.ImageField(
        upload_to=image_upload_to, null=True, blank=True,
        verbose_name='Аватарка'
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='taplink',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Таплинк'
        verbose_name_plural = 'Таплинк'

    def __str__(self):
        return str(self.user)

    def get_absolute_url_for_owner(self):
        return reverse('shop-owner', kwargs={'shop_owner': self.pathname})

    def get_absolute_url_for_customer(self):
        return reverse('shop-customer', kwargs={'shop_customer': self.pathname})


class Editor(models.Model):
    editor = models.TextField(verbose_name='Editor')
    taplink = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='editors',
        verbose_name='Таплинк'
    )

    class Meta:
        verbose_name = 'Редактор'
        verbose_name_plural = 'Редакторы'

    def __str__(self):
        return self.editor


class Messenger(models.Model):
    telegram = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Telegram'
    )
    title_t = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Название Telegram'
    )
    whatsapp = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='WhatsApp'
    )
    title_wa = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Название WhatsApp'
    )
    taplink = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='messengers',
        verbose_name='TapLink',
    )

    class Meta:
        verbose_name = 'Мессенджер'
        verbose_name_plural = 'Мессенджеры'

    def __str__(self):
        if self.telegram and self.whatsapp:
            return f'TapLink: {self.taplink} - ' f'Telegram: {self.telegram}' \
                   f' - WhatsApp: {self.whatsapp}'
        elif self.telegram:
            return f'TapLink: {self.taplink} - Telegram: {self.telegram}'
        elif self.whatsapp:
            return f'TapLink: {self.taplink} - WhatsApp: {self.whatsapp}'
        else:
            return f'TapLink: {self.taplink}'


def create_save_taplink(sender, instance, created, **kwargs):
    if created:
        TapLink.objects.create(user=instance)
        instance.taplink.save()


post_save.connect(create_save_taplink, sender=CustomUser)
