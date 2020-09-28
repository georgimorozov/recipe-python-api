from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating new user with email is successful.
        :return:
        """
        email: str = 'test@test.com'
        password: str = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test email for new user is normalized.
        :return:
        """
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating email with no user raises error.
        :return:
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """
        Test Creating a new SuperUser
        :return:
        """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'password123'
        )

        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
