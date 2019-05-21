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

def runCar(carName, x):
    carName.turtle.penup()
    carName.turtle.goto(x,carName.speed/2)
    carName.turtle.pendown()
    carName.turtle.fillcolor(carName.color)
    carName.turtle.begin_fill()

    for i in range(20):
        carName.drive()
        carName.left_turn()

    carName.turtle.end_fill()

if __name__ =="__main__":
    register_shape("car.gif")

    dadcar = Car(200, "red", "E-class")
    runCar(dadcar,-500)

    momcar = Car(400, "blue", "E-class")
    runCar(momcar,-200)

    mycar = Car(100, "yellow", "E-class")
    runCar(mycar,300)
