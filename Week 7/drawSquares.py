# Samat
# 11/8/2026
# Problem 5 - Uses the drawSquare function to draw 5 squares, one inside
# another, each one 20 pixels bigger than the last.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

squareSize = 20
for i in range(5):
    drawSquare(alex, squareSize)
    squareSize = squareSize + 20

    # Move 10 pixels down and 10 pixels left so the next, bigger square
    # is centered around the one just drawn
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

wn.exitonclick()
