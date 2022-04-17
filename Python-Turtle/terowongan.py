import turtle as t 
import random


t.speed("fast")
t.hideturtle()
t.bgcolor("black")

counter = 0
while counter < 120:
    t.pencolor("cyan")
    t.penup()
    t.goto(0,0)
    t.forward(200)
    t.pendown()
    t.circle(100)
    t.left(2)
    
    counter+=1
