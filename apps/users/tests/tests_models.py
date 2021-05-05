from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class CustomUserTestCase(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(
            phone_number='+123456',
            password='testpass123456'
        )
        self.admin_user = User.objects.create_superuser(
            phone_number='+12345678',
            password='testpass12345678'
        )

    def test_is_user_exists(self):
        self.assertEqual('+123456', self.user.phone_number)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_is_superuser_is_exists(self):
        self.assertEqual('+12345678', self.admin_user.phone_number)
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
