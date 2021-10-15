
from django.contrib.auth import get_user_model
from django.http import response
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from django.test.client import Client

from accounts.views.registration import LoginView, SignupView

USER_MODEL = get_user_model()

class LoginTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = {'email': 'test@gmail.com', 'password': 'touparet'}
        self.user_cache = USER_MODEL.objects.create_user(**self.credentials)

    def test_can_access_login_page(self):
        request = self.factory.get(reverse('accounts:login'))
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_can_login(self):
        client = Client()
        response = client.post(reverse('accounts:login'), data=self.credentials)
        # We should be redirected to the home page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_can_signup(self):
        client = Client()
        credentials = {'email': 'test@gmail.com', 'password': 'touparet'}
        response = client.post(reverse('accounts:signup'), data=credentials)
        self.assertEqual(response.status_code, 200)
        user = USER_MODEL.objects.get(email='test@gmail.com')
        self.assertEqual(user.email, 'test@gmail.com')

    def test_should_sinup_if_account_exists(self):
        client = Client()
        response = client.post(reverse('accounts:signup'), data=self.credentials)
        self.assertEqual(response.status_code, 302)
