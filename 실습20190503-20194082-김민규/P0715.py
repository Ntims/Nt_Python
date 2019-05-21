import turtle

def tree(length):
    if length > 5:
        t.forward(length)
        t.right(40)
        tree(length-15)
        t.left(80)
        tree(length-15)
        t.right(40)
        tree(length-15)
        t.backward(length)

t = turtle.Turtle()
t.left(90)

t.color("green")
t.speed(10)
tree(90)
