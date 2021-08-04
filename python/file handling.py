'''
opening a file 
open(filename,mode)

r = reading
w = writing
a = appending 

'''

#Writing a file 
vacationPlaces = ['London', 'Paris','New York', 'Rome']
vacationFile = open('My file.txt', 'w')

for x in vacationPlaces:
    vacationFile.write(x + ' ' + '\n')

vacationFile.close()

# Reading a file
readingFile = open('My file.txt', 'r')

for line in readingFile:
    print(line)

readingFile.close()

#Reading lines
readingFile2 = open('My file.txt', 'r')

firstline = readingFile2.readline()
print(firstline)

secondline = readingFile2.readline()
print(secondline)



readingFile2.close()


#Appending in a file 
myFile = open('My file.txt', 'a')
final = input('What do you want to append?')
myFile.write('\n' + final)
myFile.close()








