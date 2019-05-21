import math

class CirclePrivate:
    # Construct a circle object
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius

if __name__ == "__main__":
    c = CirclePrivate(5)
    print("Radius=", c.getRadius())
    print("Perimeter=", c.getPerimeter())
    print("Ared=", c.getArea())

    c.setRadius(5.4)
    print("Radius=", c.getRadius())
    print("Perimeter=", c.getPerimeter())
    print("Area=", c.getArea())
