import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()

move(-200,0)
square(100)
move(0,0)
square(100)
move(200,0)
square(100)
