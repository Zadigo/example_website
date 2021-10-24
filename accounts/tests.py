
from django.contrib.auth import get_user_model
from django.http import response

from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.test.client import Client

from accounts.views.registration import LoginView, SignupView

USER_MODEL = get_user_model()

class AuthenticationTests(TestCase):
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
        credentials = {
            'email': 'fast.fashion@yopmail.com',
            # 'password': 'touparette',
            'password1': 'touparette',
            'password2': 'touparette',
            'lastname': 'test',
            'firstname': 'test'
        }
        response = client.post(reverse('accounts:signup'), data=credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('accounts:login'))
        # user = USER_MODEL.objects.get(email=credentials['email'])
        # self.assertEqual(user.email, credentials['email'])
        # self.assertFalse(user.is_active)

    def test_should_sinup_if_account_exists(self):
        client = Client()
        response = client.post(reverse('accounts:signup'), data=self.credentials)
        self.assertEqual(response.status_code, 302)

    def test_signup_logic(self):
        credentials = {
            'email': 'pehir17061@bomoads.com',
            'password': 'touparette',
            'lastname': 'test',
            'firstname': 'test'
        }
        request = self.factory.post(reverse('accounts:signup'), data=credentials)
        response = SignupView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_can_activate_account(self):
        client = Client()
        attrs = {'uidb64': 'MjM', 'token': 'av0qtg-46984941573024d4a7ca3299bd0ee759'}
        response = client.get(reverse('accounts:activation', kwargs=attrs))
        self.assertEqual(response.status_code, 200)
