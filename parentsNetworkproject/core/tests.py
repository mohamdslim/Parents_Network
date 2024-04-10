from django.test import TestCase,Client
from django.contrib.auth import get_user_model,authenticate, login
from .models import Task, Schedule
from datetime import time
from django.urls import reverse

User = get_user_model()

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        test_user = User.objects.create_user(username='testuser', password='12345')
        Task.objects.create(user=test_user, text='Test Task', completed=False)

    def test_task_text(self):
        task = Task.objects.get(id=1)
        expected_text = f'{task.text}'
        self.assertEqual(expected_text, 'Test Task')

    def test_task_completed_default(self):
        task = Task.objects.get(id=1)
        self.assertFalse(task.completed)


class ScheduleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        Schedule.objects.create(parent=test_user, week='1', week_days='Monday', type='Study', task='English', duration=time(9, 0))

    def test_schedule_str(self):
        schedule = Schedule.objects.get(id=1)
        expected_str = f'{schedule.task}-{schedule.parent}'
        self.assertEqual(expected_str, 'English-testuser')

    def test_schedule_week_day(self):
        schedule = Schedule.objects.get(id=1)
        self.assertEqual(schedule.week_days, 'Monday')

    def test_schedule_type(self):
        schedule = Schedule.objects.get(id=1)
        self.assertEqual(schedule.type, 'Study')


class LoginPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user for login
        cls.user = User.objects.create_user(username='testuser', password='12345')

    def setUp(self):
        # Set up the client for making requests
        self.client = Client()

    def test_login_page_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_page_post_valid_credentials(self):
        # Test login with valid credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('profile'))

    def test_login_page_post_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertRedirects(response, reverse('login'))  # Redirect back to login page
        # You can also check if the appropriate error message is shown in the context

    def test_login_page_authenticated_user(self):
        # Test behavior when user is already authenticated
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('login'))
        self.assertRedirects(response, reverse('profile'))