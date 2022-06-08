from math import *


class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    @property
    def radius (self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def calculate_area(self):
        square = round((self.radius ** 2) * pi, 2)
        return square

    def info(self):
        print(f'Circle radius: {self.radius} {self.unit}, area: {self.calculate_area()} sq {self.unit}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        self.__side_b = value

    def calculate_area(self):
        square = round((self.side_a * self.side_b) * 0.5, 2)
        return square

    def info(self):
        print(f'Right Triangle side a: {self.side_a} {self.unit}, side b: {self.side_b} {self.unit}'
              f' area: {self.calculate_area()} sq {self.unit}')


def create_figures():
    circle1 = Circle(3)
    circle2 = Circle(5)
    triangle1 = RightTriangle(5, 7)
    triangle2 = RightTriangle(8, 10)
    triangle3 = RightTriangle(12, 15)
    list = [circle1, circle2, triangle1, triangle2, triangle3]
    return list

for i in create_figures():
    i.info()
