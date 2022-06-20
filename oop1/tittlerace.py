from turtle import Turtle
from random import randint

#create object
leo = Turtle('turtle')
leo.color('blue')
leo.penup()
leo.goto(-100,70)
leo.pendown()

dona = Turtle('turtle')
dona.color('Yellow')
dona.penup()
dona.goto(-160,70)
dona.pendown()

Raphael = Turtle('turtle')
Raphael.color('Green')
Raphael.penup()
Raphael.goto(-170,70)
Raphael.pendown()

Michaelangelo = Turtle('turtle')
Michaelangelo.color('Red')
Michaelangelo.penup()
Michaelangelo.goto(-180,70)
Michaelangelo.pendown()

for move in  range(100):
    leo.forward(randint(1,5))
    dona.forward(randint(1,5))
    Raphael.forward(randint(1,5))
    Michaelangelo.forward(randint(1,5))