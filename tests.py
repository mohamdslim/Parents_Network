from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Profile
from .views import settings

User = get_user_model()

class SettingsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.profile = Profile.objects.create(users=self.user, id_user=self.user.id, bio='Test bio', location='Test location')

    def test_settings_view_get(self):
        request = self.factory.get(reverse('settings'))
        request.user = self.user
        response = settings(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'setting.html')

    def test_settings_no_image(self):
        request = self.factory.post(reverse('settings'), {'bio': 'Updated bio', 'location': 'Updated location'})

        request.user = self.user
        response = settings(request)

        self.assertEqual(response.status_code, 302)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio')
        self.assertEqual(self.profile.location, 'Updated location')

