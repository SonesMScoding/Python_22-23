import random

def SonesBogoSort(a):
    def isSorted(a):
        if len(a) < 2:
            return True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True

    while not isSorted(a):
        a[0] = 11
        random.shuffle(a)
        #the assignment of a[0] being 11 will mess this algorithm up. 
        
    return a


num1 = input('Input  comma separated numbers:\n').strip()
a = [int(item) for item in num1.split(',')]


print(SonesBogoSort(a))
