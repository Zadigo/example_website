from django.test import TestCase
from django.test.client import Client, RequestFactory
from rest_framework.test import RequestsClient, APIClient

from api.views.todos import get_todos


class TestTodosView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_can_get_todos(self):
        request = self.factory.get('/todos')
        response = get_todos(request)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        client = APIClient()
        response = client.get('/todos')
        self.assertEqual(response.status_code, 200)
