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

    #clears session for new game
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
    """Performs the main game tasks: checks letters in word, checks for 
    winner and loser, and updates session."""

    #request letter guessed from temp_doc.html
    guessed_letter = request.form.get("guess-letter")

    #flash message incase user enters a letter already guessed
    #otherwise, update session with guess
    if guessed_letter in session['all_guesses']:
        flash('You already guessed that!')
    else:
        all_guesses_list = session['all_guesses']

        all_guesses_list.append(guessed_letter)

    #calls helper function to check if letter is in word
    show = check_guessed_letter(guessed_letter)
    
    #updates session to show letter guessed in word
    session['show'] = show

    #calls helper function to update attempts left
    guesses_left = incorrect_guesses_left(guessed_letter)

    #updates session with guesses remaining
    session['guesses_left'] = guesses_left

    #calls helper function and checks for winner
    winner = check_winner(guesses_left)

    #if winner, takes user to landing page
    if winner:
        message = "Congrats! You won!"
        return render_template('play_again.html', message=message)
    
    #checks for loser
    loser = check_loser(guesses_left)

    #if loser, takes user to landing page
    if loser:
        message = "Sorry! You ran out of incorrect guesses."
        return render_template('play_again.html', message=message)

    return redirect('/game-status')


@app.route("/check-word", methods =['POST'])
def guessed_word():
    """Checks if word entered by user is a match. If word guessed is incorrect,
    update session with guess and redirect to game board."""

    #request guessed word
    guessed_word = request.form.get("guessed-word").lower()

    #call helper function to see if word is a match
    is_match = check_guessed_word(guessed_word)

    #if word is a match, render landing page to play again
    #else, alert incorrect guess and update attempts
    if is_match:
        message = "You guessed the word right! You won!"
        return render_template('play_again.html', message=message)
    else:
        flash('Sorry! Incorrect guess.')
        all_guesses = session['all_guesses'].append(guessed_word)
        session['guesses_left'] -= 1
        guesses_left = session['guesses_left']
    
    #checks if user ran out of trys after incorrectly guessed word
    is_loser = check_loser(guesses_left)

    #if is loser, redirect to landing page
    if is_loser:
        message = "Sorry! You ran out of incorrect guesses."
        return render_template('play_again.html', message=message)

    #in all other cases, game continues
    return redirect('/game-status')


@app.route("/play-again", methods=['POST'])
def play_again():
    """Redirects player from landing page to play again."""

    return redirect('/')

    

#############################################
# HELPER FUNCTIONS


def check_guessed_letter(guessed_letter):
    """Checks if letter guessed and creates game display."""

    #shows if guessed letter is found is word
    #hides letters that have not been guessed yet
    show = ''

    for letter in session['word']:
        if letter in session['all_guesses']:
            show += letter
        else:
            show += ' _ '

    return show

def check_guessed_word(guessed_word):
    """Checks if guessed word is a match."""

    is_match = False

    if guessed_word == session['word'] and session['guesses_left'] > 0:
        is_match = True
    else:
        is_match = False

    return is_match


def check_winner(guesses_left):
    """Checks if user won."""

    winner = False

    #if word matches all correctly guessed letters and attempts remain
    if session['word'] == session['show'] and session['guesses_left'] > 0:
        winner = True

    return winner

def check_loser(guesses_left):
    """Checks if user lost."""

    loser = False

    #if no attempts remaining, user lost
    if session['guesses_left'] == 0:
        loser = True

    return loser


def incorrect_guesses_left(guessed_letter):
    """Finds the number of incorrect guesses left."""

    guesses_left = 6
    
    #decrements guesses left when letter guessed not in word 
    for letter in session['all_guesses']:
        if letter in session['word']:
            pass
        else:
            guesses_left -= 1

    return guesses_left



if __name__ == "__main__":
    
    app.debug = True
    app.run(host="0.0.0.0")
  
