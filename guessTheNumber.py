#!usr/bin/python3

import random

secretNumber = random.randint(1, 20)
print('I am thinking a number between 1 and 20.')

for guessTaken in range(1, 7):
	print('Take a guess.')
	try:
		guess = int(input())
	except ValueError:
		print("That wasn't a number!")
    
	if(guess < secretNumber):
		print('Your guess is too low.')
	elif(guess > secretNumber):
		print('Your guess is too high.')
	else:
		break

if(guess == secretNumber):
	print('Good Job! you guessed my number in ' + str(guessTaken) + ' guesses!')
else:
	print('Nope. The I was thinking of was ' + str(secretNumber))



