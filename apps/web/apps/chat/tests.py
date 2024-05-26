from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ChatRoom

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.home_url = reverse('home')
        self.room_url = reverse('room', args=['testroom'])
        self.room_list_view_url = reverse('room_list_view')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/enter_room.html')

    def test_room_GET(self):
        ChatRoom.objects.create(name='testroom', user=self.user)
        response = self.client.get(self.room_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/room.html')

    def test_room_list_view_GET(self):
        response = self.client.get(self.room_list_view_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/room_list.html')