import tabulate

userfile = input("Enter the file name: ")

i = open(userfile, "r")

text = i.readlines()
i.close()

for line in text:
    data = line.split()
    print(tabulate(data, headers=["Name", "Hours", "Total Pay"]))
    



