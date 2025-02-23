def readfile(filename):
    with open (filename, 'r') as f:
                for line in f:
                    print(line)
                    
def findFile (pathname, d):
                indent=''
for i in ranged(d):
                indent = indent + ''

if (os.path.isdir(pathname)):
    for item in os.listdir(pathname):
        newItem = os.path.join(pathname, item)

print(indent+newItem)

if(os.path.isdir(newItem)):
    findFile(newItem, d + 1)

else: 
    print(indent + pathname)
    
    readFile(pathname)
findFile('tests\hello.txt', 0)