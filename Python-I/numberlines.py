userinput = input("Enter an input file name>> ")
useroutput = input("Enter an output file name>> ")

text = ["This is the first line of text.", "This is the second line of text.", "This is the third line of text.", "This is the fourth line of text."]

iw = open(userinput, "w")
for lineOfText in text:
	iw.write(lineOfText)
 
iw.close()



op = open(useroutput,'w')

num=0
for lineOfText in text:
    x = num + 1
    op.write(str(x) + "> " + lineOfText + '\n')
    num = int(x)
    
op.close()
