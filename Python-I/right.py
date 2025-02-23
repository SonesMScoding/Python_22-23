import math   
   
avalue = int 
bvalue = int
cvalue = int
   
aside = int(input("Enter the first side: "))
bside = int(input("Enter the second side: "))
cside = int(input("Enter the third side: "))
    
    
 
   ## The Pythagorean theorem states that given a right triangle:

    ##hypotenuse squared equals the sum of the sides squared.
    ##c**2 = a**2 + b**2
    
   ## WAYS OF FINDING HYPOTENUSE 
    ##c = math.sqrt(a ** 2 + b ** 2) 
    ##<< how to find the c = v```a^2 +b^2```
    
    
cvalue = math.sqrt(aside ** 2 + bside ** 2)
avalue = math.sqrt(cside ** 2 + bside ** 2)
bvalue = math.sqrt(cside ** 2 + aside ** 2)
if cvalue == cside or avalue == aside or bside == bvalue:
    print("The triangle is a right triangle")
    
elif aside == bside == cside:
    print("The triangle is not a right triangle")

elif aside==bside or bside==cside or cside==aside:
    print("The triangle is not a right triangle")

else :
    print("The triangle is not a right triangle")
    
