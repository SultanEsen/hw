import fractions


class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        self.__denominator = value

    def __str__(self):
        return f'{fractions.Fraction(self.__numerator, self.__denominator)}'

    def __add__(self, other):
        return f'Sum of these numbers: ' \
               f'{fractions.Fraction(self.__numerator, self.__denominator) + fractions.Fraction(other.__numerator, other.__denominator)}'

    def __sub__(self, other):
        return f'Sub of these numbers: ' \
               f'{fractions.Fraction(self.__numerator, self.__denominator) - fractions.Fraction(other.__numerator, other.__denominator)}'

    def __mul__(self, other):
        return f'Multiplication of these numbers: ' \
               f'{fractions.Fraction(self.__numerator, self.__denominator) * fractions.Fraction(other.__numerator, other.__denominator)}'

    def __floordiv__(self, other):
        return f'FloorDivision of these numbers: ' \
               f'{fractions.Fraction(self.__numerator, self.__denominator) // fractions.Fraction(other.__numerator, other.__denominator)}'



num1 = Fraction(15, 16)
num2 = Fraction(9, 22)
print(f'1st number: {num1}, 2nd number: {num2}\n')
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)