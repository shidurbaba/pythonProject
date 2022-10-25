import readWrite

file = open('text.txt')

#Real all the contents of the file

#print(file.read()) #reads the entire text file

#Reads line by line

#Print line by line using while method
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()

lines = file.readlines()

for listOfLines in lines:
    print(listOfLines)

file.close()
