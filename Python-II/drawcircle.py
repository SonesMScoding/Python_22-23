#Write your program below:

from turtle import Turtle
import math
def drawCircle(t, x, y, r):
    t.up()
    t.goto(x+r, y)
    t.down()
    t.setheading(90)
    for count in range(120):
        t.left(3)
        t.forward(2*math.pi*r/120)

def main():
    t=Turtle()
    drawCircle(t, 50, 75, 100)

if name == "main":
    main()
