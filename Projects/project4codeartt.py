import turtle

# first shape
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("deeppink")
turtle.Screen().bgcolor("thistle")
t.pendown()

for i in range(50):
    t.forward(40+i)
    t.left(72)

#second shape

import turtle

t = turtle.Turtle()
t.penup()
t.goto(-200,-200)
t.color("fuchsia")
t.pendown()

for i in range(80):
    t.forward(30+i)
    t.left(45)

#third shape
t = turtle.Turtle()
t.penup()
t.goto(100, -100)
t.color("deeppink")
turtle.Screen().bgcolor("thistle")
t.pendown()

for i in range(50):
    t.forward(40+i)
    t.left(72)

#fourth shape
import turtle

t = turtle.Turtle()
t.penup()
t.goto(200,-200)
t.color("fuchsia")
t.pendown()

for i in range(80):
    t.forward(30+i)
    t.left(45)

#fifth shape
import turtle

t = turtle.Turtle()
t.penup()
t.goto(100,200)
t.color("fuchsia")
t.pendown()

for i in range(80):
    t.forward(30+i)
    t.left(45)

#sixth shape
import turtle
t.penup()
t.goto(200,100)
t.color("deeppink")
turtle.Screen().bgcolor("thistle")
t.pendown()

for i in range(50):
    t.forward(40+i)
    t.left(72)

turtle.exitonclick()