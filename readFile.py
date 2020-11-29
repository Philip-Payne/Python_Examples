'''
fo = open("myFile.txt", "r")
print(fo.read())
fo.close()
'''

import random

def getRandomLine ():
    x = random.randint(1, 7776)
    return (lines[x])

fo=open('word_list.txt', 'r')
lines=fo.readlines()


for i in range (5):
    print (getRandomLine ())

fo.close()
