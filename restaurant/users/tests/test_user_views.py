from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserCreateTests(APITestCase):
    def test_post_user(self):
        url = reverse('create_user')

        response = self.client.post(url, data={'username': 'user', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post(url, data={'email': 'user', 'username': 'user', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, data={'email': 'user@user.com', 'username': 111, 'password': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'email': 'user@user.com',
            'username': 'user',
            'password': 'password'
        }

        url = reverse('create_user')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class JwtTokenTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user@user.com', 'username', 'password')
        self.user.save()

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_obtain_blacklist_jwt_token(self):
        response = self.client.post(reverse('token_obtain_pair'), data={'email': 'user@user.com', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        refresh_token = response.data['refresh']

        response = self.client.post(reverse('token_refresh'), data={'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(reverse('blacklist'), data={'refresh_token': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
