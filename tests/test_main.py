import unittest
from app.main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bem-vindo', response.data)

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

if __name__ == '__main__':
    unittest.main()