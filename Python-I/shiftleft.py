# Put your code here
import string




Left = str
CharsToL = str
NumOfChar = int
UserStringL = str(input("Enter a string of bits: "))


NumOfChar = len(UserStringL)

if NumOfChar > 1:

    UserStringL[2:-1] = CharsToL
    UserStringL[0:1] = Left
    
    print(CharsToL, Left)
