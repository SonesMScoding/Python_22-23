def drawKochFractal(width, height, size, level):

    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()

    drawFractalLine(t, size, 0, level);
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)

def drawFractalLine(t, distance, th, level):

    if (level == 0):
        drawPolarLine(t, distance, th)
    else:
        drawFractalLine(t, distance//3, th, level - 1)
        drawFractalLine(t, distance//3, th + 60, level - 1)
        drawFractalLine(t, distance//3, th - 60, level - 1)
        drawFractalLine(t, distance//3, th, level - 1)


def drawPolarLine(t, distance, th):

    t.setheading(th)
    t.forward(distance)

def main():
    level = 4
    drawKochFractal(200, 200, 150, level)

main()
