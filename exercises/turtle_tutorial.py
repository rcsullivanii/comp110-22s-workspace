"""Designing triangular graphics by importing turtle."""

from turtle import Turtle, colormode, done

# from pyrsistent import b

leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

colormode(255)
leo.color((9, 255, 0), "pink")

leo.up()
leo.goto(-150, -129.9)
leo.down()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color("green", "purple")

bob.speed(50)
bob.hideturtle()

bob.up()
bob.goto(-150, -129.9)
bob.down()

side_length: float = 300
j: int = 0
DECREASING_FACTOR = 0.99
while (i < 100000):
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * DECREASING_FACTOR
    j = j + 1

done()
