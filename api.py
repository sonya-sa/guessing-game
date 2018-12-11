import requests
import random

WORD_LINK = 'http://app.linkedin-reach.io/words'


def get_word(difficulty=1):


    """calls LinkedIn API and creates a dictionary of words by difficulty by calling LinkedIn API"""

        
    payload = {"difficulty": difficulty}

    #calls API to get list of words at certain difficulty
    #Returns: <Response [200]>
    r = requests.get(WORD_LINK,params=payload)

    #binds a list of words to a variable
    word_list = r.text.split('\n')

    #get word at difficult level
    word = random.choice(word_list)

    return word

print get_word(difficulty=1)
