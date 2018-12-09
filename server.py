from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
#from flask_debugtoolbar import DebugToolbarExtension

from word_dict import get_word
import requests
import random

#create an instance of the flask app.
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')

@app.route("/select-difficulty")
def word_by_difficulty():
    """Retrieves difficulty level when user selects a number between 1-10."""

    difficulty = request.args.get("difficulty")
    return difficulty

@app.route("/secret-word")
def get_secret_word(difficulty):

    secret_word = get_word(difficulty)
    return render_template(secret_word=secret_word)

  

if __name__ == "__main__":
    #set to True for debugging
    #set to False for production
    app.debug = True

    app.run(host="0.0.0.0")
