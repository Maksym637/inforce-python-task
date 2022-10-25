from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class MenuTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user@user.com', 'username', 'password')
        self.user.save()
    
    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_get_menus(self):
        url = reverse('menus')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_menu(self):
        url_restaurant = reverse('create_restaurant')
        url_menu = reverse('create_menu')

        # login :
        self.client.login(email='user@user.com', password='password')

        # creating a restaurant :
        self.client.post(url_restaurant, data={"name": "smth", "contact_phone": "smth", "address": "smth"}, format='json')

        # creating a menu :
        data_correct = {
            "votes": 10,
            "restaurant": 1
        }
        response = self.client.post(url_menu, data=data_correct, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_incorrect = {
            "votes": 10,
            "restaurant": "..."
        }
        response = self.client.post(url_menu, data=data_incorrect, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
