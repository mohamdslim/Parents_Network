from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.urls import reverse
from myapp.views import YourFormView
from myapp.forms import YourForm


class YourFormViewTests(TestCase):
    def test_form_valid(self):
        request = RequestFactory().post(reverse('your_form_view_url'),
                                        data={})
        user = User.objects.create(username='testuser')
        form = YourForm(data={}, instance=user)
        form.is_valid = lambda: True
        view = YourFormView()
        view.request = request
        response = view.form_valid(form)

        self.assertRedirects(response,
                             reverse('profile_url'))
