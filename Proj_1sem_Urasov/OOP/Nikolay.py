
class TraingleChacer():
        def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        def is_triangle(self):
            if type(self.side1) == str or type(self.side2) == str or type(self.side3) == str:
                return "введите числа"
            elif self.side1 < 0 or self.side2 < 0 or self.side3 < 0:
                return "из отричательного треугольник не построить"
            elif self.side1 == 0 or self.side2 == 0 or self.side3 == 0:
                return "треугольник не построить"
            return "Ура можно постоить реугольник"

TriangleOne = TraingleChacer("YU", 0, 0)
print(TriangleOne.is_triangle())
print(type(str))
