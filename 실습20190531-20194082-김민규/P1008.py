from turtle import *
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("car.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

if __name__ == "__main__":
    register_shape("car.gif")

    myCar = Car(100, "yellow", "E-class")
    myCar.turtle.penup()
    myCar.turtle.goto(100,0)
    myCar.turtle.pendown()
    myCar.turtle.fillcolor(myCar.color)
    myCar.turtle.begin_fill()

    for i in range(20):
        myCar.drive()
        myCar.left_turn()

    myCar.turtle.end_fill()
