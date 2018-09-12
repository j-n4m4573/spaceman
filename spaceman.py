
from turtle import *

## If the guessed letter is in the mystery word, the position(s)
## of the letter(s) are revealed in the placeholders.
## If a guessed letter occurs more than once in the word all the places that letter occurs are revealed.
## If a player guesses all the letters in the word, they win the game.
## For each incorrect guess a part of the Spaceman (a 7 part drawing of a Spaceman) is drawn.
## If all 7 parts of the Spaceman are drawn then the player loses the game.

## add mystery word
## take user input letter
## add to mystery guess list
## check to see if letter is in mystery word
## if letter is in mystery word then add to nice choice list.. then
## display letter on screen
## if letter is not in mystery word then display on screen and add to other
## choice listself.
## repeat ask for letter and check to see if letter is in the mystery word
## Game finishes when user reaches seven missed letters

mystery_word = "mystery"
user_guesses = []
nice_guess = []
wrong_guess = []
counter = 0
rev_guess = ['_','_','_','_','_','_','_']

def choose_letter():
    user_guess = input("Pick a letter... guess the mystery word (7 letters)  _ _ _ _ _ _ _  ")
    checkGuess(user_guess)

def checkGuess(user_guess):
    for letter in mystery_word:
        if user_guess == letter:
            rev_guess[mystery_word.find("{}".format(letter))] = "{}".format(letter)
            print(" ".join(rev_guess))
            nice_guess.append(user_guess)
            user_guesses.append(user_guess)
            print("Goood choice buddy!! {} is on our list ".format(user_guess))
            gameEngine()
    else:
        wrong_guess.append(user_guess)
        print("sorry buddy,{} is not on our list".format(user_guess))
        print(wrong_guess)
        gameEngine()

def gameEngine():
    keep_it_going = True
    while keep_it_going:
        if len(wrong_guess)  == 7:
            keep_it_going = False
            print("end game")
        else: choose_letter()


gameEngine()
# chooseLetter()

# grab index of letter and place spaces around it
# _ _ s _ _ _
# hold the position of the correct letters and display the on the screen

# when an index is chosen reveal the letter in a formated string
# array holding revealed letters and blank spots for the indexes without the
# the numbers revealed
# how can we turn spaces into letters and non spaces into blank spaces
