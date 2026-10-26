# Samat
# 10/25/2026
# Asks the user for the number of sides, side length, line color and fill color,
# then draws the regular polygon and fills it in.

import turtle

numSides = int(input("Enter the number of sides: "))
sideLength = int(input("Enter the length of each side: "))
lineColor = input("Enter the line color: ").strip().lower()
fillColor = input("Enter the fill color: ").strip().lower()

wn = turtle.Screen()
polygonTurtle = turtle.Turtle()
polygonTurtle.pensize(3)
polygonTurtle.pencolor(lineColor)
polygonTurtle.fillcolor(fillColor)

polygonTurtle.begin_fill()
for side in range(numSides):
    polygonTurtle.forward(sideLength)
    polygonTurtle.left(360 / numSides)
polygonTurtle.end_fill()

wn.exitonclick()
