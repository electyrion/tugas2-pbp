import unittest
from django.test import TestCase, Client


class TestViews(TestCase):

    def test_show_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEquals(response.status_code, 200)

    def test_show_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEquals(response.status_code, 200)

    def test_show_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
