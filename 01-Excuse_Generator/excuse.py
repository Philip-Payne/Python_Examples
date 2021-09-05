# This is a simple script that demonstrates a few basic principles in Python
# There is no user input. Each time the code runs a new random excuse is generated

# Import any modules we need later
# we can rename these if we want to using 'as'
from random import choice as pick

'''
The excuse we want to generate is similar to

I'm sorry I'm late but there were | a million | cats | by my car

The basic form of this is

I'm sorry I'm late but there were | QUANTITY | OBJECT | LOCATION

So we have three parts that we can randomise.
'''

# The lists
quantityList=['loads of', 
              'like, a million', 
              'ten thousand', 
              'a bunch of', 
              'a shed load of']
objectList=['cats', 
            'Wombles', 
            'pink elephants', 
            'apple turnovers', 
            'cheese crisps']
locationList=['in my car', 
              'under my bed', 
              'on the road', 
              'in my room', 
              'down the shops']

# Pick a random element from each list 
qty=pick(quantityList)
obj=pick(objectList)
loc=pick(locationList)

# Print out the excuse
print("I'm sorry I'm late but there were " + qty + " " + obj + " " + loc + ".")
