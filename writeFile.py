counter = 0
outputString = ""
while counter < 100:
    outputString = outputString + "\n" + str(counter)
    counter += 1


fo = open("myFile.txt", "w")
#fo.write("This is new content in a file")
fo.write(outputString)
fo.close()
