# Pseudocode

## Introduction
There are no rules with pseudocode, you need to find a system that works for you and works with the language you intend to use. Pseudocode is a tool to help you think about and plan your code. While there ae no rules here are a few guidlines...

1. Keep it simple
2. Don't make it look like a known language
3. Be consistant

Lastly, do not try to write a long program in Pseudocode. The benefit of Pseudocode typically comes from working on small sections of code.


## Command Statements/Commands
```python
# Input from a user or other program/device
input
# Set a variable to a specific value
set
# Output a message of some form - print to screen but could also be sending data to
# another part of the program.
output 
# An itterative loop 
loop n from x to y step z ... next n
# Conditional loops
while something is true ... loop
do ... while something is true
# Conditional statements
if ... else if ... else ... end if
# Additional items
# Text (Strings) are placed in quotes 
"My name is Philip"
# Numbers do not have quotes 
5, 3.14, 100000
```

## Examples

```python
# Print the words "Hello, World"
output "Hello, World!"
```

```python
# Add two numbers and print out the result
set result to 3 plus 4
output result
```

```python
# Print the sum, difference and product of two numbers

set a to 3
set b to 4

output "The sum of the two numbers is ", a plus b
output "The difference of the two numbers is ", a minus b
output "The product of the two numbers is ", a times b
```

```python
# print all the numbers from 1 to 10

loop n from 1 to 10 step 1
    output n
next n
```

```python
# Add up all the numbers from 1 to 10 and print the total

set total to zero
loop from 1 to 10 step 1
    add n to total
next n

output total
```

```python
# Draw a grid of five stars in five rows like this
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

loop n from 1 to 5 step 1
    output "* * * * *"
next n
```

```python
# As above but for any number

input n "What size grid would you like to print?"
loop row from 1 to n step 1
    loop col from 1 to n step 1
        output "* "
    next col
    output new line
next row
```