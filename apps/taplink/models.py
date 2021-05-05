from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

from apps.taplink.utils import image_upload_to


CustomUser = get_user_model()


class TapLink(models.Model):
    url = models.SlugField(
        unique=True, null=True, blank=True, verbose_name='URL'
    )
    avatar = models.ImageField(
        upload_to=image_upload_to, null=True, blank=True,
        verbose_name='Avatar'
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='taplinks',
        verbose_name='User'
    )

    def __str__(self):
        return str(self.user)


class TapLinkEditor(models.Model):
    editor = models.TextField(verbose_name='Editor')
    taplink = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='taplink_editors',
        verbose_name='TapLink'
    )

    def __str__(self):
        return self.editor


class TapLinkMessenger(models.Model):
    telegram = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Telegram'
    )
    whatsapp = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='WhatsApp'
    )
    taplink = models.ForeignKey(
        to=TapLink, on_delete=models.CASCADE, related_name='taplink_messengers',
        verbose_name='TapLink',
    )

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
        instance.taplinks.save()


post_save.connect(create_save_taplink, sender=CustomUser)
