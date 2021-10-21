from django.test import TestCase
from django.shortcuts import reverse
from django.test.client import Client

class TestLegalPages(TestCase):
    def setUp(self):
        self.client = Client()

    def test_can_visit_privacy(self):
        response = self.client.get(reverse('legal:privacy'))
        self.assertEqual(response.status_code, 200)

    def test_can_visit_terms_of_use(self):
        response = self.client.get(reverse('legal:terms_of_use'))
        self.assertEqual(response.status_code, 200)

    def test_can_visit_terms_of_conditions(self):
        response = self.client.get(reverse('legal:terms_of_conditions'))
        self.assertEqual(response.status_code, 200)

    def test_can_visit_about_us(self):
        response = self.client.get(reverse('legal:about_us'))
        self.assertEqual(response.status_code, 200)
