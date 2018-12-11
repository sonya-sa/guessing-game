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

    session.clear()
    return render_template('index.html')

@app.route("/start-game")
def start_game():
    """Automatically select a word for user to guess and display it."""

    difficulty = request.args.get("select-difficulty")
    #calls api from api module and starts game at level 1
    word = get_word(difficulty)

    #create session to keep track of new game
    session['word'] = word
    session['all_guesses'] = []
    session['show'] = ' '
    # session['incorrect_guesses'] = ''
    # session['correct_guesses'] = ''
    # session['num_guesses_left'] = MAX_GUESSES
    # session['all_guesses'] = ''
    # session['display'] = len(word) * '_'

    return redirect('/game-status')

@app.route("/game-status")
def render_game_status():
    """This function renders template to show the updated game board."""

    display = session['show']

    check_winner(display)

    return render_template('temp_doc.html', display=display)

@app.route("/guess-letter", methods=['POST'])
def play_game():

    guessed_letter = request.form.get("guess-letter")

    all_guesses_list = session['all_guesses']

    all_guesses_list.append(guessed_letter.encode('utf-8'))

    #session['all_guesses'] = all_guesses_list

    check_guessed_letter(guessed_letter)

    return redirect('/game-status')


# @app.route("/display-word")
# def display_word():

#     display = len(session['word']) * ' _'

#     return render_template('temp_doc.html',display=display)

# @app.route("/check-letter")
# def guessed_letter():

#     guessed_letter = request.args.get("guessed-letter").lower()

@app.route("/check-word")
def guessed_word():

    guessed_word = request.args.get("guessed-word").lower()

    if guessed_word == session['word']:
        return redirect('/winner')
    else:
        session['all_guesses'] += guessed_word
        INCORRECT_GUESSES += 1
        flash('Sorry! Incorrect guess.')

    return redirect('/game-status')

@app.route("/winner")
def winner():

    win_message = "Congrats! You won."

    return render_template("play_again.html", win_message=win_message)

@app.route("/play-again")
def play_again():

    play_again = request.args.get("play-again")

    return redirect("/")

    


# @app.route("/select-difficulty")
# def word_by_difficulty():
#     """Retrieves word by difficulty level when user selects a level between 1-10."""

#     difficulty = request.args.get("difficulty")
#     word = get_word(difficulty)
#     return word

# @app.route("/guesses-left")
# def guesses_left():


# @app.route("/check-guess")
# def check_guess():
    

#############################################
# HELPER FUNCTIONS


def check_guessed_letter(guessed_letter):

    show = ''

    for letter in session['word']:
        if letter in session['all_guesses']:
            show += letter
        else:
            show += ' _ '

    session['show'] = show

def check_winner(display):
    
    if session['word'] == display:
        return redirect('/winner')
    else:
        pass
      
# def check_letter(guessed_letter):

#     all_guesses = session['guesses']

#     while not WINNER and INCORRECT_GUESSES < MAX_GUESSES:

#         if guessed_letter in all_guesses:

#             flash("You already guessed that! Try again.")
#         else:
#             for: 


# def incorrect_guesses_left(word, guesses):
    # """Finds the number of incorrect guesses left."""

#     num_wrong = 0
#     for letter in word:
#         if letter in word:
#             pass
#         else:
#             num_wrong += 1

#     return num_wrong



if __name__ == "__main__":
    
    app.debug = True
    app.run(host="0.0.0.0")
  
