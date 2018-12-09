# # #create a word guessing game where the user play the "computer"
# # #user has a maximum of 6 tries to guess correctly

import random
import requests
#create a function that randomly selects a word
# def get_word(difficulty):
#     """Selects a secret word for game."""
 
#     # wordlist = ['hello']
#     # return random.choice(wordlist).lower()
#     difficulty = input('Select difficulty. Choose a number between 1-10: ')
#     return word
WORD_LINK = 'http://app.linkedin-reach.io/words'

def get_word(difficulty=1):

    """calls LinkedIn API and creates a dictionary of words by difficulty by calling LinkedIn API"""

    words = {}

    if difficulty not in words:
        
        payload = {"difficulty": difficulty}

        #calls API to get list of words at certain difficulty
        #Returns: <Response [200]>
        r = requests.get(WORD_LINK,params=payload)

        #binds a list of words to a variable
        word_list = r.text.split('\n')

        words[difficulty] = word_list

    #get word at difficult level
    selected = random.choice(words[difficulty])

    return selected


#create function that checks word and guess
#function has 3 paramaters: word selected, guess letter, list of guesses taken
def check(word, guesses, guess):
    """Checks guessed letter and shows all correctly guessed letters and remaining spaces."""
    show = ''
    matches = 0

    for letter in word:
        if letter == guess:
            matches += 1
        if letter in guesses:
            show += letter
        else:
            show += '-'
    if matches > 1:
        print('Yes, there are {} {}'.format(matches,guess) + "'"+ 's in the word.')
    elif matches == 1:
        print ('Yes! The word contains the letter: ' + guess + "'")
    else:   
        print (show)
        print ('Sorry. The word does not contain the letter "' + guess + '".')

    return show

#main function that runs game
def main():
    difficulty = input('Select a difficulty. Choose a number between 1-10: ')
    #call get_word function and assign to word variable
    word = get_word(difficulty)
    #print(word)
    guesses = []
    guessed = False
    incorrect = 0
    max_guesses = 6

    while not guessed and incorrect < max_guesses:
        text = 'Please enter one letter or a {}-letter word: '.format(len(word))
        print('You have already guessed: {}'.format(guesses))
        guess = input(text).lower()
        
        #if we already guessed the letter, try again
        if guess in guesses:
            print('You already guessed:' + guess + ". Try again.")
        
        #check word for match
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            
            #word was incorrect guess
            else:
                incorrect += 1
                print ('Sorry! That is incorrect.')
        
        elif len(guess) == 1:
            guesses.append(guess)

            #returns a string of checked guesses
            result = check(word,guesses,guess)
            
            #if guess not in return string, then letter was incorrect 
            if guess not in result:
                incorrect += 1
            elif result == word:
                guessed = True
            else:
                print(result)
        else:
            print('Invalid entry.')
    
    if incorrect == max_guesses:
        print ('Sorry! You hit the maximum incorrect guesses. You lose.')
    
    else:
        print ('Yes, the word is', word + '. It took you', len(guesses), 'tries.')

main()

