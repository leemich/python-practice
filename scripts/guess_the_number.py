#!/usr/bin/python
#
# Coding Challenge - Guess the Number Game
#
# Create a simple game where the computer picks
# a number between 1 - 100 and asks the player
# to guess the number.
#
# Calculate the number of guess, let the player
# know if they won and how many guesses they took
# and inform them of the number if they fail to 
# guess it in the specified number of tries.
#
# https://www.reddit.com/r/beginnerprojects/comments/19jj9a/project_higherlower_guessing_game/

from random import randrange

print('''Welcome to my Guess the Number Game!

	I am thinking of a number between 1 and 100.
	Guess the number in 8 tries, and you win!''')

def guess_num():
	while True:
		guesses_taken = 0
		secret_num = randrange(1, 101)
		while guesses_taken < 8:
			print()
			print('What is your guess?')
			guess = int(input('> '))
			guesses_taken += 1
			if guess == secret_num:
				break
			elif guess > secret_num:
				print('Your guess is too high. Guess again!')
			elif guess < secret_num:
				print('Your guess is too low. Guess again!')


		if guess == secret_num:
			print('Congratulations! You guessed my number in ' + str(guesses_taken) + ' guesses!')


		if guess != secret_num:
			print('You failed to guess the secret number!')
			print('The number I was thinking of was ' + str(secret_num) + '.')

	print('Would you like to play again?')
	print('Type yes or no:')
	cont_choice = input('> ')
	if cont_choice.lower() == 'y':
		print('I am thinking of a number between 1 and 100. Guess the number in 8 tries, and you win!')
		continue
	else:
		print('Thank you for playing!')
		break

guess_num()
