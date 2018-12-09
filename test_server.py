from unittest import TestCase
from server import app
import server

class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do done before every test."""

        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during test
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertTrue('index.html')


if __name__ == "__main__":
    
    import unittest

    unittest.main()