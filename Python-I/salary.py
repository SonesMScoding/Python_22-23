salary = float(input("Enter the starting salary: "))
annualperc = int (input("Enter the annual percentage increase: "))
years = int (input("Enter the number of years: "))

for count in range (years - 1):
    
    
    ## salary = 30,000
    ##annual% = 2%
    ##years over time = 10
    
    ## (30,000 * .2) + 30,000 = year one salary
    ## (Salary * annual%) + salary = one iteration
    
    startsalary = salary
for count in range(years - 1):
        salary = salary * annualperc
        startsalary = startsalary + 2 * salary 

startsalary = startsalary + salary * annualperc