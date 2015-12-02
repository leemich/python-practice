#!/usr/bin/python
#
# Coding Challenge - Guess the Numbr Game

from random import randrange
import sys

while True:
    guesses_taken = 0
    secret_num = randrange(1, 50)
    while guesses_taken < 7:
        print('What number am I thinking of? (Press Q to quit.)')
        guess = input('> ')
        if guess.lower() == 'q':
            print('Thank you for playing!')
            sys.exit()
        guesses_taken += 1
        guess = int(guess)
        if guess < secret_num:
            print('Your guess is too low.')
        elif guess > secret_num:
            print('Your guess is too high.')
        elif guess == secret_num:
            print('Congratulations! You guessed my number in ' + str(guesses_taken) + ' guesses!')
            print()
            print('Would you like to play again? Y/N')
            play_again = input('> ')
            if play_again.lower() == 'y':
                break
            elif play_again.lower() == 'n':
                print('Thank you for playing!')
                sys.exit()
        else:
            break
    if guess != secret_num:
        print()
        print('I\'m sorry. The number I was thinking of was ' + str(secret_num) + '.')
        print()
        print('Would you like to play again? Y/N')
        play_again = input('> ')
        if play_again.lower() == 'y':
            continue
        elif play_again.lower() == 'n':
            print('Thank you for playing!')
            sys.exit()
        
