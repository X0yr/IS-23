import math

class Traingle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def type(self):
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            return "Не треугольник"
        if self.side1 == self.side2 == self.side3:
            return "треугольник равносторонний"
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "треугольник равнобедренный"
        return "обычный треугольник"

    def square(self):
        self.p = (self.side1 + self.side2 + self.side3)/2
        return math.sqrt(self.p * (self.p - self.side1) * (self.p - self.side2) * (self.p - self.side3))

TriangleOne = Traingle(0, 0, 0)
print(TriangleOne.type())
print(TriangleOne.square())
