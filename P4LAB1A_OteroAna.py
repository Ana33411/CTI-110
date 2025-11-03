# Ana Otero
# P4LAB1A - Shapes
# This program draws a square and a triangle using loops

import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("P4LAB1A - Shapes")

artist = turtle.Turtle()
artist.shape("turtle")
artist.pensize(3)
artist.color("purple")

for side in range(4):
    artist.forward(100)
    artist.left(90)

artist.penup()
artist.goto(150, 0)
artist.pendown()
artist.color("green")

count = 0
while count < 3:
    artist.forward(100)
    artist.left(120)
    count += 1

turtle.done()