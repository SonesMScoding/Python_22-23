inputLyst = input('Enter elements of a list separated by space ')
print("\n")
lyst = inputLyst.split()
# print list


for i in range(len(lyst)):
    # convert each item to int type
    lyst[i] = int(lyst[i])
    
mode = float
mean = float
median = float



def my_mode(sample):
    mode = max(set(sample), key=sample.count)
    return mode

def my_mean(sample):
    mean = sum(sample) / len(sample)
    return mean

def my_median(sample):
    n = len(sample)
    index = n // 2
     # Sample with an odd number of observations
    
    if n % 2:
         return sorted(sample)[index]
     # Sample with an even number of observations
     
    return sum(sorted(sample)[index - 1:index + 1]) / 2


median = my_median(lyst)
mean = my_mean(lyst)
mode = my_mode(lyst)

print("List: " , lyst)
print("Mode: " , mode)
print("Median: " , median)
print("Mean: " , mean)
