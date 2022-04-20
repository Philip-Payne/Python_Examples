# Improvements

There are two main areas where the game could be improved.

## Range

At the moment the game sets a secret number between 1 and 100. To make the game more difficult you could change the range to between 1 and 1000. At the moment you would have to change this in two places, in the description of the game and the 'randint' function. To solve this problem create a variable that holds the upper limit and replace the two instances of the number 100 with the variable. You could, alternatively, ask the user to input the upper limit so they could select the game difficulty.

## Input Errors

The game will not function properly if the user does not input an integer. You would need to add some error checking to the input statement to correct this. This is a very common issue with writing computer programs but is a little too complex for an introductory example. 