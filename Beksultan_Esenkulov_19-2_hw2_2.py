class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def __calculate_perimeter(self):
        pass

    def info(self):
        pass

    @property
    def calculate_perimeter(self):
        return self.__calculate_perimeter()


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.perimeter = self.calculate_perimeter()

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter

    def side_length(self, value):
        self.__side_length = value

    def calculate_perimeter(self):
        return self.side_length * 4

    def calculate_area(self):
        return self.side_length ** 2

    def info(self):
        print(f'Square side lenght: {self.side_length} {self.unit}, perimeter: {self.perimeter} {self.unit}'
              f', area: {self.calculate_area()} sq {self.unit}')


class Rectangle(Figure):
    def __init__(self, lenght, width):
        super().__init__()
        self.__lenght = lenght
        self.__widht = width
        self.perimeter = self.calculate_perimeter()

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value

    @property
    def widht(self):
        return self.__widht

    @widht.setter
    def widht(self, value):
        self.__widht = value

    def calculate_perimeter(self):
        return (self.lenght + self.widht) * 2

    def calculate_area(self):
        return self.lenght * self.widht

    def info(self):
        print(f'Rectangle lenght: {self.lenght} {self.unit}, width: {self.widht} {self.unit}, '
              f'perimeter: {self.perimeter} {self.unit}'
              f', area: {self.calculate_area()} sq {self.unit}')

def create_figures():
    square1 = Square(3)
    square2 = Square(7)
    rectangle1 = Rectangle(5, 7)
    rectangle2 = Rectangle(8, 9)
    rectangle3 = Rectangle(10, 12)
    list = [square1, square2, rectangle1, rectangle2, rectangle3]
    return list


for i in create_figures():
    i.info()