from django.test import TestCase
from django.contrib.auth.models import User , logout
from django.urls import reverse


def test_logout_user(request):
    # ודא שהמשתמש מחובר
    user = request.user
    self.assertTrue(user.is_authenticated)

    response = logout_user(request)

    self.assertFalse(user.is_authenticated)

    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, reverse('login'))

#  3 בדיקות יחידה מ כלי AI
# Cloude.AI
#1 unittest 1
class SignupViewTest(TestCase):

    def test_signup_user(self):
        # הכנת נתוני משתמש
        data = {
            'username': 'mohamad',
            'email': 'mohamad.2@gmail.com',
            'password1': 'Moh12345',
            'password2': 'Moh12345',
        }

        response = self.client.post(reverse('signup'), data=data)

        # בדיקת יצירת משתמש חדש
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(username='mohamad')

        # בדיקת התחברות אוטומטית
        self.assertTrue(self.client.login(username='mohamad', password='Moh12345'))

        # בדיקת הפניית משתמש לדף הפרופיל
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('profile'))

#Unittest 2


class SignupViewTest(TestCase):

    def test_signup_user_with_mismatched_passwords(self):
        # הכנת נתוני משתמש
        data = {
            'username': 'mohamad',
            'email': 'mohamad.2@gmail.com',
            'password1': 'Moh12345',
            'password2': 'Moh12345',
        }

        response = self.client.post(reverse('signup'), data=data)

        # בדיקת אי יצירת משתמש חדש
        self.assertEqual(User.objects.count(), 1)

        # בדיקת קבלת שגיאה
        self.assertFormError(response, 'form', 'username', 'This username is already taken.')




# Unittest 3



class SignupViewTest(TestCase):

    def test_signup_user_with_existing_username(self):
        User.objects.create_user(username='test_user', password='password1234')

        # הכנת נתוני משתמש
        data = {
            'username': 'mohamad',
            'email': 'mohamad.2@gmail.com',
            'password1': 'Moh12345',
            'password2': 'Moh12345',
        }

        response = self.client.post(reverse('signup'), data=data)

