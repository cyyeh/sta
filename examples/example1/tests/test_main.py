import unittest

from ..main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data, b'Hello, World!')
