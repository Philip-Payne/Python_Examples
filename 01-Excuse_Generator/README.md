# Excuse Generator

The excuse generator is a short program that generates a random excuse. In a very basic way this is an example of a natural language system although, obviously, natural language systems are typically far more complex.

This example includes the use of imported modules, lists and concatenation in a print statement.

## Importing Modules

As part of the code we will want to pick a random element from a list. All the random functions are contained within the 'random' module. We could import all the random functions with...

```python
import random
```

and then we can use any of the functions such as the 'choice' function with...

```python
myStr = random.choice(myList)
```

But we normally do not want access to all the functions in a module so we should just import the ones we need with...

```python
from random import choice
```

The code now becomes

```python
myStr = choice(myList)
```

We can also rename a function if we wish like this...

```python
from random import choice as pick
```

and the code becomes

```python
myStr = pick(myList)
```

Generally it is not a good idea to rename a function unless it either helps to improve the readability of our code or avoids some naming conflict with other modules.

## Lists

Lists in Python are similar to indexed arrays in other languages. You can create a list in a number of different ways but for this example we will populate the list at the start of the code (at declaration) like this...

```python
myList = ["item 1", "Item 2", "Item 3"]
```

Lists do not have to contain strings. Lists can contain other data types such as integers or other lists.

Once you have created a list your code can change it. Technically we say that a list in Python is mutable. This is not true of some other data collections in Python or indexed arrays in some other languages. This is one of the things you have to learn for each language.

## Printing

We often need to combine literal strings and variables in a print statement. This is reasonably straightforward but there are some points to note. If we have the following code...

```python
firstString = "Hello"
secondString = "World"

print (firstString + " " + secondString + ", my name is Philip.")
# prints out "Hello World, my name is Philip."
```

Joining together strings is called concatenation. In Python the concatenation operator is the + symbol. When we concatenate the two variable we need to put a space between them - this is a very common thing to do. If you look at the literal string at the end of the print statement you will see it starts with a comma. This is to make the punctuation appear in the correct place. You will always need to consider this when printing strings.

## The Excuse Generator Pseudocode

```python
# Import any modules we need later
import the choice function from the random module

'''
The excuse we want to generate is similar to

I'm sorry I'm late but there were a million cats by my car.

The basic form of this is

I'm sorry I'm late but there were | QUANTITY | OBJECT | LOCATION.

So we have three parts that we can randomise.
'''

# The lists
set quantityList to a list of quantities # "loads of", "hundreds of" etc
set objectList to a list of objects # "cats", "banana splits", "apples" etc
set locationList to a list of locations # "in my car", "on the road" etc

# Pick a random element from each list 
set qty to a random choice from quantityList
set obj to a random choice from objectList
set loc to a random choice from locationList

# Print out the excuse
output "I'm sorry I'm late but there were " + qty + " " + obj + " " + loc + "."
```

Try to write your own version of the program from the notes above and the pseudocode. If you get stuck try creating a program with one list and print out a random choice from that list.

When you are done have a look at the code in the python file here and see how it compares to your code. You could also look at the notes on improving and extending your code.