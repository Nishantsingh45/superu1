from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile

class UserProfileAPITest(APITestCase):

    def setUp(self):
        self.create_url = reverse('create-or-update-profile')
        self.update_url = reverse('create-or-update-profile')

        self.valid_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

    def test_create_profile(self):
        response = self.client.post(self.create_url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().email, self.valid_data['email'])

    def test_update_profile(self):
        profile = UserProfile.objects.create(email='test@example.com', first_name='John', last_name='Doe')

        update_data = {
            'id': profile.id,
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }

        response = self.client.patch(self.update_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().email, update_data['email'])
        self.assertEqual(UserProfile.objects.get().first_name, update_data['first_name'])
        self.assertEqual(UserProfile.objects.get().last_name, update_data['last_name'])
