from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .user_manager import UserManager


class CustomUser(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(
        _('Phone number'), unique=True, max_length=20
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()
