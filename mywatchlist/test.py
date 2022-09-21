import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Movie, Watchlist


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_POST(self):
        response = self.client.post(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


if __name__ == '__main__':
    unittest.main()
