from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """ class to Test models """
    def test_create_user_with_email_succesfull(self):
        """testing new user with email is succesfull """
        email = 'test@gmail.com'
        password = 'test.1234'
        user = get_user_model().objects.create_user(
                          email=email,
                          name='test',
                          password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """testing user email normalize """
        email = 'test1@GMAIL.COM'
        user = get_user_model().objects.create_user(
                       email=email,
                       name='test',
                       password='test.123'
        )
        self.assertEqual(user.email,email.lower())

    def test_user_invalid_email(self):
        """tesing given user no email raise error"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email=None,name='test',password='test.123')

    def test_create_new_super_user(self):
        """testing creating new superuser"""
        user = get_user_model().objects.create_superuser(
                             email='test1@gmail.com',
                             name='test',
                             password='test.1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
