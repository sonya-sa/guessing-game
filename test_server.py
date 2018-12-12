from unittest import TestCase
from server import app
from flask import session
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
        self.assertIn("Difficulty level", result.data)
        self.assertIn("Guessing-Game", result.data)
        self.assertEqual(result.status_code, 200)
        self.assertTrue('index.html')

class FlaskRouteTests(unittest.TestCase):
    """Tests Flask routes"""

    def setUp(self):
       """Stuff to do done before every test."""

        #Get the Flask test client.
        self.client = app.test_client()
        #Show Flask errors during test.git stat
        app.config['TESTING'] = True

        #set up session with parameters to test
        with self.client as c:
            with c.session_transaction() as sess:
                sess['word'] = 'fun'
                sess['all_guesses'] = ['a']
                sess['show'] = 3
                sess['guess_left'] = 4

    def test_start_game(self):

        result = self.client.get("select-difficulty", query_string={'difficulty': 1}, follow_redirects=True)
        self.assertIn('_', result.data)
        self.assertEqual(200, result.status_code)
        self.assertTrue('intex.html')
        self.assertIsInstance(result.data, str)

        #test checks guesses left on page, can do the same with 3 ""
        self.assertTrue(4, result.data) 


    def test_render_game_status(self):
        pass

    
    # def test_play_game(self):

    #     """Test "/guess-letter" route."""

    #     #tests post method
    #     result = self.client.post("/login")

    # def test_guessed_word(self):
    #     pass

    # def test_play_again(self):
    #     pass


class FlaskRouteGuess(unittest.TestCase):
    """Tests Flask routes"""

    def setUp(self):
        """Stuff to do done before every test."""

        #Show Flask errors during test.
        app.config['TESTING'] = True
        #Get the Flask test client.
        self.client = app.test_client()

        # set up session with parameters to test 
        # Can test for winner by setting up sample winner input 
        with self.client as c:
            with c.session_transaction() as sess:
                sess['word'] = 'fun'
                sess['all_guesses'] = ['a', 'u', 'f']
                sess['show'] = " f u _"
                sess['guesses_left'] = 4


    def test_win(self):
        result = self.client.get("/game-status", data = {'guess-letter': 'u'}, follow_redirects=True)
        self.assertIn("Congrats! You won!", result.data)


if __name__ == "__main__":pyth
    
    import unittest

    unittest.main()