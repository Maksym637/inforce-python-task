from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class RestaurantTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user@user.com', 'username', 'password')
        self.user.save()
    
    def tearDown(self):
        self.client.logout()
        self.user.delete()
    
    def test_get_restaurants(self):
        url = reverse('restaurants')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_restaurant(self):
        url = reverse('create_restaurant')

        data = {
            "name": "smth",
            "contact_phone": "smth",
            "address": "smth"
        }

        self.client.login(email='wrong', password='wrong')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(email='user@user.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
