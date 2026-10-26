# Samat
# 10/25/2026
# Draws a semi truck driving on a road under the sun using turtle graphics.

import turtle

wn = turtle.Screen()
wn.title("Semi Truck")
wn.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Sun
pen.penup()
pen.goto(220, 150)
pen.dot(90, "gold")

# Sun rays
for ray in range(12):
    pen.goto(220, 150)
    pen.setheading(ray * 30)
    pen.forward(55)
    pen.pendown()
    pen.pencolor("orange")
    pen.pensize(3)
    pen.forward(25)
    pen.penup()

# Road
pen.goto(-350, -110)
pen.setheading(0)
pen.color("dimgray")
pen.begin_fill()
for side in range(2):
    pen.forward(700)
    pen.right(90)
    pen.forward(120)
    pen.right(90)
pen.end_fill()

# Lane stripes
pen.color("white")
pen.pensize(5)
for stripeX in range(-340, 350, 80):
    pen.penup()
    pen.goto(stripeX, -170)
    pen.pendown()
    pen.forward(40)
pen.penup()

# Trailer
pen.pensize(2)
pen.pencolor("black")
pen.fillcolor("white")
pen.goto(-250, -70)
pen.setheading(0)
pen.pendown()
pen.begin_fill()
for side in range(2):
    pen.forward(300)
    pen.left(90)
    pen.forward(130)
    pen.left(90)
pen.end_fill()
pen.penup()

# Company name on the trailer
pen.goto(-100, 5)
pen.color("navy")
pen.write("CSS 225 FREIGHT", align="center", font=("Arial", 20, "bold"))

# Cab
pen.pencolor("black")
pen.fillcolor("red")
pen.goto(60, -70)
pen.setheading(0)
pen.pendown()
pen.begin_fill()
pen.forward(110)
pen.left(90)
pen.forward(60)
pen.left(30)
pen.forward(35)
pen.left(60)
pen.forward(80)
pen.left(90)
pen.forward(90)
pen.end_fill()
pen.penup()

# Cab window
pen.goto(115, 5)
pen.setheading(0)
pen.fillcolor("lightcyan")
pen.pendown()
pen.begin_fill()
pen.forward(40)
pen.left(90)
pen.forward(25)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(25)
pen.end_fill()
pen.penup()

# Wheels
for wheelX in [-220, -170, 0, 80, 140]:
    pen.goto(wheelX, -95)
    pen.setheading(0)
    pen.pencolor("black")
    pen.fillcolor("black")
    pen.pendown()
    pen.begin_fill()
    pen.circle(22)
    pen.end_fill()
    pen.penup()
    pen.goto(wheelX, -84)
    pen.dot(14, "silver")

wn.exitonclick()
