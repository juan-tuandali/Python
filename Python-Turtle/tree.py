import turtle as t 

t.speed("fastest")
t.bgcolor("black")
t.pensize(3)

def tree(branch,t):
    if branch > 4:
        t.forward(branch)
        t.right(20)
        tree(branch-15,t)
        t.left(40)
        tree(branch-15,t)
        t.right(20)
        t.backward(branch)
def main():
    done = t.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    tree(105,t)
    done.exitonclick()
main()
