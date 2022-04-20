# Prime Number Checker

This example is far more concerned with understanding a problem than with computer programming. We want to create a function that checks if a number is a prime number. At school you probably learned that...

> "A prime number is any number only divisible by one and itself"

Unfortunately this is only part of the story.

Any number is divisible by any other number for example

```
5 / 2 = 2.5
```

But 5 is a prime number so what do we actually mean?

What we actually want are the "Integer Factors" of a number. These are the the integers, that when multiplied together give you the number you are interested in. If the Integer factors are only 1 and the number you are testing then you have a prime number - sort of.

There is more to come. The actual definition of a prime number starts with

> "A number greater than one"

So 1, 0 and any negative numbers cannot be prime numbers. This is a definition that mathematicians use. You could look up why this makes sense.

So our correct definition of a prime number is

> "A prime number is an integer, greater than one, whose only integer factors are one and itself"

This example includes the use of imported modules, user defined functions and conditional statements.

## Importing Modules

We saw how to import a module in a previous example. Tis time we are going to import the 'math' module so we can take the square root of a number.

## User Defined Function

we want to create a function to test if a number is prime. There is not a function that will do this built into Python so we have to make our own. We use the 'def' keyword to create a function, give the function a name and then put a list of parameters inside brackets. In this case there is only one parameter.

```python
def is_prime(x):
```

All the code for our function goes under this line but, like most structures in Python, we need to indent the code in the function.

## How the function works

There are several specific cases we need to deal with at the start of our function.

1. We need to check if our number is equal to or less than 1. If it is we want to return false (Not a prime).
2. We need to check if the number is 2. If it is then we return true because 2 is a prime number.
3. We want to check if our number is even (has a factor of 2) because then we can quickly reduce the number of factors to test by half.

After that we have to test to see if there is any odd number that is a factor of our test number.

** This section needs some more explanation **




## The is_Prime Function Pseudocode

```python
# Import any modules we need later
import the math module

define the function is_prime with one parameter, x

If x is less than or equal to 1 return false

if x is 2 return true

If x is even return true

set limit to the square root of x plus 1

for n from 3 to limit step 2
    if n is a factor of x return false	
loop

# The tests above have not returned so x must be prime
return true
```

Try to write your own version of the program from the notes above and the pseudocode.

When you are done have a look at the code in the python file here and see how it compares to your code. You could also look at the notes on improving and extending your code.