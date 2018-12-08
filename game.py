# #create a word guessing game where the user play the "computer"
# #user has a maximum of 6 tries to guess correctly

# import random
# #import words from word_dict

# words = ['hello', 'bye']

# class Game:
#     """Game rules and logic."""

#     def __init__(self, words):
#         self.word = random.choice(word_list)
#         self.max_incorrect_guesses = 6

#     #function gets word
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


import random

#create a list of possible words for the game
wordlist = ["frazzled", "grogginess", "crypt", "ostracize", "oxygen", \
            "rhythmic", "pajama", "jinx", "yacht", "banjo", "awkward", \
            "zigzag", "twelfth", "unzip", "mystify", "jukebox"]

random.choice(wordlist).lower()

word = list(wordlist[0])

display = []

used = []

display.extend(word)


#used.extend(display)