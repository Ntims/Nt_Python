import turtle
t= turtle.Turtle()
t.shape("turtle")

def draw(x,y):
    t.goto(x,y)

t.pensize(10)
s = turtle.Screen()
s.onscreenclick(draw)
