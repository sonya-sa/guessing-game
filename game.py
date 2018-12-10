import random
import requests
from api import get_word
#create a function that randomly selects a word


#create function that checks word and guess
#function has 3 paramaters: word selected, guess letter, list of guesses taken
def check(word, guesses, guess):
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

    #logic for calling linkedin API in api.py
    word = get_word(input('Choose a difficulty level between 1-10: '))
    #print(word)
    guesses = []
    guessed = False
    incorrect = 0
    max_guesses = 6

    while not guessed and incorrect < max_guesses:
        text = 'Please enter one letter or a {}-letter word: '.format(len(word))
        print('Letters already guessed: {}'.format(guesses))
        print ()
        print ('You have {} incorrect guesses remaining.'.format(max_guesses-incorrect))
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
        print ('Sorry! You hit the maximum attempts. You lose.')
    
    else:
        print ('Yes, the word is', word + '. It took you', len(guesses), 'tries.')

main()

