from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gambs.com',
            password='adminpassword123',
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gambs.com',
            password='testpassword123',
            name='Test User'
        )

    def test_users_listed(self):
        """
        Test that users are listed on the user admin page
        """

        admin_url = reverse('admin:core_user_changelist')
        response = self.client.get(admin_url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """
        Test that the user edit page works
        """

        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_user_add_page(self):
        """
        Test that the user add page works
        """

        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
