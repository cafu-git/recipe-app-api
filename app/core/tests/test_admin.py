from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import pytest


@pytest.mark.django_db
class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@admins.org",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@testusers.org",
            password="password123",
            name="TestUser"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # admin/core/user/<int:id>/change/
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user works"""
        url = reverse('admin:core_user_add')
        # /admin/core/user/add/
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
