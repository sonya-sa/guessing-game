import unittest
from server import app
from flask import session
import server


class FlaskTestsBasic(unittest.TestCase):
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

        #Show Flask errors during test.
        app.config['TESTING'] = True
        #Get the Flask test client.
        self.client = app.test_client()

        # set up session with parameters to test 
        with self.client as c:
            with c.session_transaction() as sess:
                sess['word'] = 'fun'
                sess['all_guesses'] = ['a']
                sess['show'] = 3
                sess['guesses_left'] = 5

    def test_start_game(self):

        # changes result to "/start_game as route, and changed difficulty to select-difficulty, 
        # added follow_redirct = True
        result = self.client.get("/start-game", query_string={'select-difficulty': 1}, follow_redirects=True)
        self.assertIn('_', result.data)
        self.assertEqual(200, result.status_code)
        self.assertTrue('intex.html')
        self.assertIsInstance(result.data, str)

        # added a test to check guesses left on page, can do the same with 3 '__' 
        # can come up with som
        self.assertTrue(4, result.data) 


    def test_render_game_status(self):
        pass


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
                sess['all_guesses'] = ['a', 'u', 'f', 'h', 'i', 'p']
                sess['show'] = "fu _"
                sess['guesses_left'] = 2


    def test_win(self):
        result = self.client.post("/guess-letter", data = {'guess-letter': 'n'})
        self.assertIn("Congrats! You won!", result.data)

    def test_lose(self):
        result = self.client.post("/guess-letter", data = {'guess-letter': 'o'})
        result = self.client.post("/guess-letter", data = {'guess-letter': 'l'})
        self.assertIn("Sorry! You ran out of incorrect guesses.", result.data)

    def test_wrong(self):
        result = self.client.post("/guess-letter", data = {'guess-letter': 'o'},\
         follow_redirects=True)
        self.assertIn('<h6>You have <span id="guesses-left"><font size="3" color="red">1</font></span> incorrect guesses left.</h6>', result.data)

    def test_word_is_match(self):
        result = self.client.post("/check-word", data = {'guessed-word': 'fun'})
        self.assertIn("You guessed the word right! You won!", result.data)




    
    # def test_play_game(self):

    #     """Test "/guess-letter" route."""

    #     #tests post method
    #     result = self.client.post("/login")

    # def test_guessed_word(self):
    #     pass

    # def test_play_again(self):
    #     pass




if __name__ == "__main__":
    
    import unittest

    unittest.main()
