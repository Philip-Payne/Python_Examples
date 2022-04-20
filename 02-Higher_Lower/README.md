# Higher Lower Game

The Higher-Lower game is a fairly common program example used when learning a computer programming language. The program selects a random number and the user is asked to guess the number. Each time the user guesses a number the program responds by saying the number is to high, too low or correct.

This example includes the use of user input, imported modules, loops and conditional statements.

## Importing Modules

We saw how to import a module in a previous example and we are going to use the 'random' module again in this example. The difference is that we want to use the 'randint' function rather than the 'choice' function because this time we want a random integer rather than a random element from a list.

To import the 'randint' function from the 'random' module we use...

```python
from random import randint
```

and then we can select a random integer with...

```python
myRandomNumber = randint(1, 100)
```

And this will select a random number between 1 and 100.

This is fine for our simple game but you should not rely on simple random number generators for anything important like security systems. There is a lot to learn about random number generation in different languages but we do not need to worry about that here.

## User Input

We often want to get a user to input something to a computer program. In Python this is quite straightforward using the 'input' function. We use the input function to print a message on the screen asking the user to type something and then whatever the user types is held in a variable like this...

```python
guess = input("Guess the secret number ")
```

Here the user will see "Guess the secret number " and then type in a number and press enter. The number will then be stored in the variable 'guess'.

We do have a problem here. The 'input' function always returns a string, but we want an integer to compare to our secret, random, number. We can solve this problem by 'Casting' the data type.

## Casting

We can change the data type of a variable by putting the data type we want in brackets before the variable or expression like this...

```python
aString = "1"
anInt = (int)aString
```

This does not always work. For example...

```python
aString = "Hello"
anInt = (int)aString
```

will not work because we cannot change a word into an integer. Again, there is a lot more to learn about casting but it can be very useful at times.

## Looping

In our game we want to keep going until the player correctly guesses the secret number. Whenever you want to keep doing something until a condition is reached you probably want a while loop. In this case we want to keep the program running while the players guess and the secret number are not the same like this...

```python
while guess != secret:
    # Do something here
```

Python expects us to indent all the code within our loop. Other languages use different methods of identifying the block of code in loops, for example, by using braces {}.

## Conditionals

The while loop is an example of a conditional programming structure but a more common example is an 'if' statement. A conditional statement relies on the condition being true or false, there are no other options. We can set up an 'if' statement so that if the condition is true one piece of code runs or "ELSE" if the condition is false another bit of code runs like this...

```python
if 'Condition"":
    # The condition is true so we run some code
else:
	# The condition is false so we run different code
```
This is called an if-eles statement. There is also an elseif statement for use with multiple conditions.


## The Higher-Lower Game Pseudocode

```python
# Import any modules we need later
import the randint function from the random module

# We will do some setup first

Set 'introduction' to the game introductory text

Set 'secret' to a random number between 1 and 100

output introduction

get guess from the user

while the secret and the guess are not the same

	if the guess is to high
		output "Your guess was too high"
	else
		output "Your guess was too low"

loop

# We are now outside the loop so the user must have guessed the secret number

output "You have won"
```

Try to write your own version of the program from the notes above and the pseudocode. If you get stuck try creating a program that just prints a random number to start.

When you are done have a look at the code in the python file here and see how it compares to your code. You could also look at the notes on improving and extending your code.