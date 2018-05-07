# Prints any line from the file with the word 'snake' in it
infile = open("test.txt", "r")
word = 'snake'
while True:
    line = infile.readline()
    if len(line) == 0:
        break
    if word in line :
        print(line, end="")
        
infile.close()
