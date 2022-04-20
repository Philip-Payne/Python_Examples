'''
This is a fairly simple game to understand and reasonably simple to code but 
probably not the first project you want to attempt. 

The program chooses a randome number between 1 and 100 and the player has to
guess tha number.

The code consists of some setup and a game loop. The only way to get out of
the loop is for the player to guess the secret number
'''

##### Initial Setup #####

# Import any modules we will need
# Later we will want a random integer in a range 
from random import randint

# Explain how the game works
introduction = '''
***********************************************
* Introduction                                *
* This program has chosen a secret number     *
* between 1 and 100.                          *
*                                             *
* You need to guess the secret number.        *
*                                             *
* Each time you guess you will be told if     *
* your guess is too high, too low or correct. *
***********************************************
'''

# Generate the secret number
secret = randint(1, 100)

# Print the introduction
print(introduction)

# Ask for the first guess
guess = int(input("Guess the secret number "))

# Keep going (loop) untill the guess is correct
while guess != secret:
    if guess>secret:
        print("Your guess was too high")
    else:
        print("Your guess was too low")
	
    guess=int(input("Guess again "))

# The guess is correct so tell the player		
print ("That is correct, the secret number is " + str(secret))
