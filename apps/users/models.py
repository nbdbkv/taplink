from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(
        _('Phone number'), unique=True, max_length=20
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("edit-profile", args=[str(self.id)])
