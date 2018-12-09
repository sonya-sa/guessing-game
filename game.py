# # #create a word guessing game where the user play the "computer"
# # #user has a maximum of 6 tries to guess correctly

# import random




# wordlist = ["hello", "bye"]

# word = random.choice(wordlist).lower()

# display = []

# used = []

# display.extend(word)

# used.extend(display)

# for i in range(len(display)):
#     display[i] = '_'

# print (' '.join(display))
# print ()


# def main():

#     counter = 0

#     incorrect = 6

#     while counter < len(word) and incorrect > 0 :

#         guess = input("Please enter a letter: ")
#         guess = guess.lower()
#         print("Number of incorrect guesses remaining: {} ".format\
#             (incorrect))

#         # if guess not in used:
#         #     used.append(guess)
#         # else:
#         #     print ("You already guessed that letter. Try again!")

#         for i in range(len(word)):

#             if word[i] == guess and guess not in used:

#                 display[i] = guess

#                 counter = counter + 1

#                 used.remove(guess)

#         if guess not in display:

#             incorrect = incorrect - 1
#             print ("Sorry, that's incorrect. You have", incorrect, \
#                 'chances remaining.')


#     if counter == len(word):
#         print ("Congratulations! You found the word.")

#     else:
#         print ("Game over.")

# main()

import random
#create a function that randomly selects a word

def get_word():
    wordlist = ['hello']
    return random.choice(wordlist).lower()

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
    #call get_word function and assign to word variable
    word = get_word()
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
        print ('Sorry! You hit the maximum trys. You lose.')
    
    else:
        print ('Yes, the word is', word + '. It took you', len(guesses), 'tries.')

main()

