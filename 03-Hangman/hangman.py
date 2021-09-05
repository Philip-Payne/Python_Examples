
''' Hangman Game
     _______
    |/      |     This is a fairly simple implementation of a hangman game.
    |      (_)    It only works with five letter words because of the
    |      \|/    limitation of the ASCII art used to draw the hangman but
    |       |     could be implemented with a more sophisticated GUI if 
    |      / \    you wanted to do something more complex.
    |
 ___|___          As a programming example this demonstrates a nice range of 
                  concepts to use in your code such as...
 									
1) Setup - Initialising the starting conditions. How do we set everything up
before we can run the actual game code?

2) Collections of data - We will use Python Lists (Similar to indexed arrays
in other languages) to hold collections of data. Specifically a list of five
letter words and a list of letters that have been correctly guessed by
the player.

3) Strings as lists - In Python you can treat a string as a list of characters.
In other languages you can (sometimes) treat a string as an array of characters.

4) Randomisation - The code needs to select a random word from the word list.
Most programming languages have some form of randomisation built in but you
need to read the details of how this works for each language.

5) User Defined Functions - We use some user defined functions to encapsulate
sections of code. This makes the code easier to read and maintain. There are
additional benefits which are not obvious in this example.

6) State - During the game play the user can be in one of three states, they
can have won, they can have lost, or they can still be playing the game. The
code must test for each state and respond appropriatly.
'''

# Import any modules we need
# We will need to make a random choice from a list later
from random import choice

#####  do any setup #####

# Declair an empty list to hold the letters guessed correctly
guessedLetters = list()
# Initialise a counter to zero to count the number of wrong guesses
wrongGusses = 0
# Initialise a list of five letter words

wordList = ["seven", "world", "about", "again", "heart", "pizza", "water",
            "happy", "sixty", "board", "month", "angel", "death", "green",
            "music", "fifty", "three", "party", "piano", "mouth", "woman",
            "sugar", "amber", "dream", "apple", "laugh", "tiger", "faith",
            "earth", "river", "money", "peace", "forty", "words", "smile",
            "house", "alone", "watch", "lemon", "south", "anime", "after",
            "santa", "women", "china"]
# Pick one random five letter word from the list
# Store the secret word in a variable
secretWord = choice(wordList)

# Setting up the display
# The scaffold is 8 rows deep (0-7).
# The figure is rows 1 to 5 counting
# from the top.
#
# 0     _______        _______
# 1    |/             |/      |
# 2    |              |      (_)
# 3    |              |      \|/
# 4    |              |       |
# 5    |              |      / \
# 6    |              |
# 7 ___|___        ___|___

# Initialise one list for the empty scaffold
# and one list for the full scaffold. The 
# elements of these lists are all strings.
emptyScaffold = ["     _______", 
                 "    |/", 
                 "    |", 
                 "    |", 
                 "    |", 
                 "    |", 
                 "    |", 
                 " ___|___"]
                 
fullScaffold = ["     _______", 
                "    |/      |", 
                "    |      (_)", 
                "    |      \|/", 
                "    |       |", 
                "    |      / \\", 
                "    |", 
                " ___|___"]
                

# The introductory text
introduction = '''
*******************************
* This is the classic Hangman *
* game. You have to guess all *
* the letters in a five       *
* letter word.                *
*                             *
* You only get five wrong     *
* guesses so make every guess *
* count.                      *
*******************************
'''

##### User Defined Functions #####

# Return the display string based on 
# the number of incorrect guesses.
# param x int: number of incorrect guesses
# return string: The hangman display	
def hangmanDisplay(x):
    # Some basic error checking
    # to make sure x is in range
    if x < 0: x = 0
    if x > 5: x = 5
    # Start with an empty string
    display = ""
    # Concaternate (add) x+1 rows from
    # the full scaffold.
    for i in range(0, x+1):
        display += fullScaffold[i] + "\n"
    # Concaternate the remaining rows
    # from the empty scaffold
    for i in range(x+2, 8):
        display += emptyScaffold[i] + "\n"
    return display

# Return a string representing the five
# letters of the word with underscores for
# letters that have not been guessed.
# Like this "W _ T _ _"
# return string: The word display
def wordDisplay():
    # Start with an empty string
    display = ""
    # Loop through all the letters in
    # the secret word
    for c in secretWord:
        # If the letter has been guessed
        # then add that letter
        if c in guessedLetters:
            display = display + " " + c
        # If the letter has not been guessed
        # add an underscore
        else:
            display = display + " _"
    return display	

# Returns a Boolean value indicating if
# the player has won.
# return bool: true if player has won
def checkForWin():
    # Loop through all the letters in 
    # the secret word
    for c in secretWord:
        # if any of the letters have not
        # been guessed by the player
        # then return false
        if c not in guessedLetters:
            return False
    # The code has worked through all the
    # letters in the secret word and not
    # returned False so return True.
    return True
	
##### The Game Code #####
	
##### start the game #####
# Print the instructions
print(introduction)
# Print out the hangman
print(hangmanDisplay(wrongGusses))
# Print out five blank spaces
print(wordDisplay())

##### Start the game loop #####
while True:
    # The player can be in one of three states,
    # they have won, lost or are still playing
    
    # State 1 - Player Win
    # If the user has guessed the word then they have won
    # Print a message and then break out of the loop to end the game
    if checkForWin():
        print("You have won. You guessed all the letters in " + secretWord)
        break
	
    # State 2 - Player Lost 
    # If the user has made 5 guesses and not got the word they have lost
    # Print a message and then break out of the loop to end the game
    if wrongGusses >= 5:
        print("You have lost. You did not guess all the correct letters.")
        print("The secret word is " + secretWord)
        break
	
    # State 3 - Player still playing
    # Get a guess from the user
    newGuess = input("Guess a letter ")
	
    # Check if the guess is in the secret word
    if newGuess in secretWord:
    # it is so add the letter to the guessed letters list
        guessedLetters.append(newGuess)
        # and print a message
        print("The letter " + newGuess + " is in the word")
    else:
        # it isn't so increment the number of wrong guesses
        wrongGusses += 1
        # and print out a message
        print("The letter " + newGuess + " is NOT in the word")
	
    # print out the hangman
    print(hangmanDisplay(wrongGusses))
    # print out the word with spaces
    print(wordDisplay())
# Loop back to start
	
# This is outside the loop and
# is the end of the game
print("\n")
print ("***** GAME OVER *****")

