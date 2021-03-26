from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'ashraf@gmail.com'
        password = 'ashraf123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = 'ashraf@GMAIL>COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test,123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
