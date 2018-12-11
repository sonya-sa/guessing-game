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

@app.route('/')
def index():
    """Homepage."""

    session.clear()
    return render_template('index.html')

@app.route("/start-game")
def start_game():
    """User selects a word to start the game."""

    #requests difficult level from user and binds to variable
    difficulty = request.args.get("select-difficulty")

    #calls api from api module
    word = get_word(difficulty)

    #creates a session to keep track of new game
    session['word'] = word
    session['all_guesses'] = []
    session['show'] = len(word) * ' _'
    session['guesses_left'] = 6

    return redirect('/game-status')

@app.route("/game-status")
def render_game_status():
    """Shows the current status of the game."""
    
    display = session['show']

    guesses_left = session['guesses_left']

    return render_template('temp_doc.html', display=display, \
        guesses_left=guesses_left)

@app.route("/guess-letter", methods=['POST'])
def play_game():
    """Requests guess from user"""

    guessed_letter = request.form.get("guess-letter")

    if guessed_letter in session['all_guesses']:
        flash('You already guessed that!')
    else:
        all_guesses_list = session['all_guesses']

        all_guesses_list.append(guessed_letter)


    show = check_guessed_letter(guessed_letter)
    
    session['show'] = show

    guesses_left = incorrect_guesses_left(guessed_letter)

    session['guesses_left'] = guesses_left

    winner = check_winner(guesses_left)

    if winner:
        message = "Congrats! You won!"
        return render_template('play_again.html', message=message)
    
    loser = check_loser(guesses_left)

    if loser:
        message = "Sorry! You ran out of incorrect guesses."
        return render_template('play_again.html', message=message)

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
        message = "You guessed the word right! You won!"
        return render_template('play_again.html', message=message)
    else:
        session['all_guesses'].append(guessed_word)
        print session['all_guesses']
        flash('Sorry! Incorrect guess.')

    return redirect('/game-status')

# @app.route("/winner")
# def winner():

#     win_message = "Congrats! You won."

#     return render_template("play_again.html", win_message=win_message)

@app.route("/play-again", methods=['POST'])
def play_again():

    play_again = request.form.get("play-again")

    return redirect('/')

    


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

    return show

def check_winner(guesses_left):

    winner = False

    if session['word'] == session['show'] and guesses_left > 0:
        winner = True

    return winner

def check_loser(guesses_left):

    loser = False

    if session['guesses_left'] == 0:
        loser = True

    return loser

# def check_loser(guesses_left):

#     if guesses_left == 0:
#         return redirect('/')




# def check_letter(guessed_letter):

#     all_guesses = session['guesses']

#     while not WINNER and INCORRECT_GUESSES < MAX_GUESSES:

#         if guessed_letter in all_guesses:

#             flash("You already guessed that! Try again.")
#         else:
#             for: 


def incorrect_guesses_left(guessed_letter):
    """Finds the number of incorrect guesses left."""

    guesses_left = 6
    
    for letter in session['all_guesses']:
        if letter in session['word']:
            pass
        else:
            guesses_left -= 1

    return guesses_left



if __name__ == "__main__":
    
    app.debug = True
    app.run(host="0.0.0.0")
  
