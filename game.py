#create a word guessing game where the user play the "computer"
#user has a maximum of 6 tries to guess correctly
import random
import requests

word_list = ['hello', 'bye']
#WORD_LINK = 'http://app.linkedin-reach.io/words'

display = []

class Game:
    """Encapsulate rules and logic of word the game"""

    def __init__(self):
        self.word = random.choice(word_list)
        self.max_incorrect_guesses = 6

    #function gets word
    #function displays spaces
    #function checks letter
    #function checks word
    #function checks guesses
    #function counts guesses
    #function counts remaining guesses
    #fuction checks winner
    #function checks loser


    # def display_spaces(self):

    #     for letter in range(len(self.word)):
    #         display[letter] = '_'
            

play = Game()

    