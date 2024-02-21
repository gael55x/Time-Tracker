from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()

class UserRegisterTestCase(APITestCase):
    """Test case for user registration."""

    def test_user_register(self):
        """Test user registration."""
        url = reverse('register')
        data = {'email': 'test@example.com', 'password': 'testpassword', 'username': 'testuser'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(UserModel.objects.get().username, 'testuser')

class UserLoginTestCase(APITestCase):
    """Test case for user login."""

    def setUp(self):
        """Set up test data."""
        self.user = UserModel.objects.create_user(email='test@example.com', password='testpassword', username='testuser')

    def test_user_login(self):
        """Test user login."""
        url = reverse('login')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserLogoutTestCase(APITestCase):
    """Test case for user logout."""

    def test_user_logout(self):
        """Test user logout."""
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserViewTestCase(APITestCase):
    """Test case for user view."""

    def setUp(self):
        """Set up test data."""
        self.user = UserModel.objects.create_user(email='test@example.com', password='testpassword', username='testuser')

    def test_user_view(self):
        """Test user view."""
        url = reverse('user')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], 'testuser')
