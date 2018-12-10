from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
#from flask_debugtoolbar import DebugToolbarExtension

from api import get_word
import requests
import random

#create an instance of the flask app.
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

MAX_GUESSES = 6
INCORRECT_GUESSES = 0
WINNER = False

@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')

@app.route("/start-game")
def start_game():
    """Automatically select a word for user to guess and display it."""

    #calls api from api module and starts game at level 1
    word = get_word(difficulty=1)

    #create session to keep track of new game
    session['word'] = word
    session['incorrect_guesses'] = ''
    session['correct_guesses'] = ''
    session['num_guesses_left'] = MAX_GUESSES
    session['guesses'] = ''
    session['display'] = len(word) * '_'

    return word

@app.route("/check-letter")
def guessed_letter():

    guess = requests.args.get("guessed-letter")

    check_letter(guess)







@app.route("/select-difficulty")
def word_by_difficulty():
    """Retrieves word by difficulty level when user selects a level between 1-10."""

    difficulty = request.args.get("difficulty")
    word = get_word(difficulty)
    return word

@app.route("/check-guess")
def check_guess():
    



#############################################
def check_letter(guess):

    guessed_letters = []

    while not WINNER and INCORRECT_GUESSES < MAX_GUESSES:

        if guess in guessed_letters:

            result['']





if __name__ == "__main__"
    
    app.debug = True
    app.run(host="0.0.0.0")
  
