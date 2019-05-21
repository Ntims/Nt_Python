import turtle

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def circle(x,y,color,radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_olympic_symbol():
    positions = [[0, 0, "blue"], [-120, 0 ,"purple"], [60, 60, "red"], [-60, 60, "yellow"], [-180,60, "green"]]
    for x,y,c in positions:
        move(x,y)
        circle(x,y,c,50)

t = turtle.Turtle()
draw_olympic_symbol()
