from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class SignInViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_signin_view_get(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')

    def test_signin_view_post_success(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, '/home/')  # Update this with your actual redirect URL upon successful login

    def test_signin_view_post_failure(self):
        data = {'username': 'nonexistentuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')
        self.assertContains(response, 'Invalid username or password.')