#create a word guessing game where the user play the "computer"
#user has a maximum of 6 tries to guess correctly
import random

word_list = ['hello', 'bye']
#WORD_LINK = 'http://app.linkedin-reach.io/words'

class Game:
    """Encapsulate rules and logic of word the game"""

    def __init__(self):
        self.word = random.choice(word_list)
        self.max_incorrect_guesses = 6
        #self.display_spaces = display_spaces()

    # @staticmethod
    # def get_word(word_list):

    #     word = random.choice(word_list)
    #     return word



    # def display_spaces(self):

    #     for letter in len(self.word):
    #         print('-')

game = Game()
print game