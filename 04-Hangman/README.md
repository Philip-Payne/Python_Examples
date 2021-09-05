# Hangman

The code for the Hangman game demonstrates a number of interesting features that you will use in other coding projects. Here are some details.

## Lists

A list is one of the main types of data collections used in Python. A list is similar to an indexed array in other languages. You can create a list in a number of ways.

```python
# This is an empty list
myFirstList = list()

# This is a list with three elements
mySecondList = ["Apple", "Orange", "Lemon"]

# You can add elements to a list with .append
mySecondList.append("Lime")

# You can access an element of a list with the index for the element
print (mySecondList[1])  # Prints Orange
# Remember that lists are zero indexed.

# You can iterate through a list with
for x in mySecondList:
    print (x)
```

There are a large number of functions that work with lists and it is worth learning some of these.

## Strings

A string can be treated as a list of characters. Not all the functions that work with lists will work with strings but it is useful to know that you can iterate through a string just like a list.

```python
myString = "Hello"

for c in myString:
    print (c)

# Will print out
# H
# e
# l
# l
# o
```

## Setup

It is common to set up a number of data structures, variables and user defined functions before you write the main body of your code. While this is important, and it is good practice to do this at the top of your code listing, we do not want to think too deeply about this before we plan our code structure. We want to know what our code is going to do before we think about the detail.

## User Defined Functions

Most programming languages allow you to create your own functions. These have two purposes. Firstly a User Defined Function (UDF) allows you to write a piece of code and then use that code in multiple locations. This is a basic principle of software development known as "DRY", or "Don't repeat yourself".

The second reason to use a UDF is that you can encapsulate (remember that word) all the code for one process in one function. In the Hangman example we use a UDF to generate the hangman display based on the incorrect number of guesses the player has made. no other part of the code relates to the display so we can go back and upgrade (or fix) the display later all in one place.

One final point about UDFs. It is good practice to return a value from a UDF rather than printing it out in the UDF. The reason for this is to separate the functionality from the display. The code here is for a command line game but if we wanted to use the same code for a mobile app the method for displaying the hangman would be different. Better to keep the function and the display separate so you can reuse the code.

## State

State is another very important concept in Computer Science & Software Engineering. We often use the example of a turnstile that can be locked or unlocked but this is sometime a bit obscure and difficult to understand.

The states in the Hangman game are a little easier to understand. The player has three possible states. They can have won, they can have lost or they can still be playing. The code needs to determine which of theses states has occurred and act accordingly.

## Pseudocode

```python
# Do any required setup
set numIncorrectGuesses to 0
set secretWord to a random five letter word
set correctlyGuessedLetters to an empty list

# The game loop
while (true)

	if (user has won)
		output "You have won"
		break out of loop

	if (user has lost)
		output "You have lost"
		break out of loop

	# The user has not won or lost so must still be playing
	# get a guess from the user
	set guess to input ("Guess a letter")
	if (guess is in secretWord)
		add guess to correctlyGuessedLetters
	else
		add 1 to numIncorrectGuesses

	output the hangman display
	output the correctly guseesd letter like this "m o _ _ h"
	
loop

# we are outside the game loop now
output "Game Over"
End
```

It isn't particularly obvious at this point where we will use our User Defined Functions. When you have a little experience with programming this will become more obvious. See the code for details.