# Ana Otero
# P4LAB1B - Initials
# Draws initials A O using turtle graphics

import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("P4LAB1B - Initials")

pen = turtle.Turtle()
pen.pensize(4)
pen.color("blue")
pen.shape("turtle")

pen.left(75)
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.backward(50)
pen.right(105)
pen.forward(30)

pen.penup()
pen.goto(120, 0)
pen.setheading(0)
pen.pendown()

pen.circle(50)

turtle.done() 