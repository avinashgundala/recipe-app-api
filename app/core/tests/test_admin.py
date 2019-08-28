from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    """testing admin site interface"""
    def setup(self):
        """setting up superuser and user for admin page access"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
                            email='admin@gmail.com',
                            name='admin',
                            password='admin.123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
                          email='test45@gmail.com',
                          name='test',
                          password='test12.1234'
        )

    def test_users_listed(self):
        """testing new user is listed in userlist"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change(self):
        """testing user change"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_user_add(self):
        """testing user add page"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
