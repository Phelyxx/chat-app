from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login_view.html')

    def test_login_view_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })

        self.assertEquals(response.status_code, 302)

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_view.html')

    def test_register_view_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'newpass123',
            'password2': 'newpass123'
        })

        self.assertEquals(response.status_code, 302)