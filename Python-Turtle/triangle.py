from turtle import *

speed(2)
pencolor("white")
bgcolor("black")

penup()
goto(-158,-100)
fillcolor("yellow")
begin_fill()
pendown()

for i in range(3):
    forward(300)
    left(120)

end_fill()
done()
