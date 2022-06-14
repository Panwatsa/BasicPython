import sys

print(sys.version)

import turtle
t = turtle.Pen()
t.shape('turtle')
def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    
def circle():
    for i in range(5):
        t.circle(60)
        t.right(90)
circle()
Go(200,200)
