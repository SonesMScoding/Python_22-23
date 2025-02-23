userinput = input("Enter an input file name>> ")
useroutput = input("Enter an output file name>> ")

iw = open(userinput, "w")
text = ("This is the first line of text.", "This is the second line of text", "This is the third line of text", "This is the fourth line of text.")

for lineOfText in text:
	iw.write(lineOfText + '\n')
 
iw.close()


op = open(useroutput,'w')
num = 0

for lineOfText in text:
    x = str(num + 1)
op.write(x + "> " + lineOfText)
num = x

op.close()
