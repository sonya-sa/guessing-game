import requests
import random

WORD_LINK = 'http://app.linkedin-reach.io/words'


# def get_word(difficulty=1):


#     """calls LinkedIn API and creates a dictionary of words by difficulty"""

#     payload = {"difficulty": difficulty}

#     #calls API to get list of words at certain difficulty
#     #Returns: <Response [200]>
#     r = requests.get(WORD_LINK,params=payload)

#     #binds a list of words to a variable
#     word_list = r.text.split('\n')

    
#     word = random.choice(word_list)

#     return word

word_dict = {}

def get_word(difficulty=1):


    """calls LinkedIn API and creates a dictionary of words by difficulty"""

    if difficulty not in word_dict:

        payload = {"difficulty": difficulty}

        #calls API to get list of words at certain difficulty
        #Returns: <Response [200]>
        r = requests.get(WORD_LINK,params=payload)

        #binds a list of words to a variable
        word_list = r.text.split('\n')

        #select word for game
        word = random.choice(word_list[0:10])

        #sets value as a dict to keep track of number of times difficulty is selected and number of times winner is chosen
        word_dict[difficulty] = {'words': word_list[0:10], 'num_diff_selected': 1 , 'num_win_at_diff': 0}

        return word
    
    else:

        word_dict[difficulty]['num_diff_selected'] += 1

        word = random.choice(word_dict[difficulty]['words'])

        return word 


# print get_word(difficulty=2)
# print get_word(difficulty=3)
# print get_word(difficulty=2)
# print word_dict

