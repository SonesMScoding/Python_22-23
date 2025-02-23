def enlarge(image, factor):
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width * factor, height * factor)
    newX = 0
    newY = 0
    oldY = 0
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            oldP = image.getPixel(x,y)
            new.setPixel(newX,newY,oldP)
            for a in range(factor):
                newX+=1
                new.setPixel(newX,newY,oldP)
        newX=0
        for b in range(new.getWidth()):
            newY=oldY
            for c in range(factor):
                oldP = new.getPixel(newX,newY)
                newY+=1
                new.setPixel(newX,newY,oldP)
            newX+=1
        oldY = newY
        newX=0
    return new

def main():
    filename = "smokey.gif"
    image = Image(filename)
    newimage = enlarge(image, 2)
    newimage.draw()

if name == "main":
   main()