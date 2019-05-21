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

    dadCar = Car(200, "red", "E-class")
    dadCar.turtle.penup()
    dadCar.turtle.goto(-500,-200/2)
    dadCar.turtle.pendown()
    dadCar.turtle.fillcolor(dadCar.color)
    dadCar.turtle.begin_fill()

    for i in range(20):
        dadCar.drive()
        dadCar.left_turn()

    dadCar.turtle.end_fill()

if __name__ == "__main__":
    register_shape("car.gif")

    momCar = Car(400, "blue", "E-class")
    momCar.turtle.penup()
    momCar.turtle.goto(-200,-400/2)
    momCar.turtle.pendown()
    momCar.turtle.fillcolor(momCar.color)
    momCar.turtle.begin_fill()

    for i in range(20):
        momCar.drive()
        momCar.left_turn()

    momCar.turtle.end_fill()

if __name__ == "__main__":
    register_shape("car.gif")

    myCar = Car(100, "yellow", "E-class")
    myCar.turtle.penup()
    myCar.turtle.goto(300,-100/2)
    myCar.turtle.pendown()
    myCar.turtle.fillcolor(myCar.color)
    myCar.turtle.begin_fill()

    for i in range(20):
        myCar.drive()
        myCar.left_turn()

    myCar.turtle.end_fill()
