class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full Name: {self.fullname}\nAge: {self.age}\nIs married: {self.is_married}\n')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks = {}):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def AVG_Rating(self):
        sum = 0
        for k, v in self.marks.items():
            sum += v
        print(f'AVG mark of {self.fullname} is {round(sum / len(self.marks), 1)}\n')


class Teacher(Person):
    salary = 100000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def total_salary(self):
        years = 0
        if self.experience > 3:
            years = self.experience - 3
            print(f'Full Name: {self.fullname}\nAge: {self.age}\nIs Married: {self.is_married}\n'
                  f'Salary: {int((years * 0.05) * self.salary + self.salary)} USD')
        else:
            print(f'Full Name: {self.fullname}\nAge: {self.age}\nIs Married: {self.is_married}\n'
                  f'Salary: {self.salary} USD')


def create_student():
    Obama_student = Student('Barack Obama', 60, 'Yes', {'Math': 6, 'Biology': 7, 'Economics': 8})
    Musk_student = Student('Elon Musk', 50, 'No', {'Math': 9, 'Biology': 8, 'Economics': 9})
    Macron_student = Student('Emmanuel Macron', 44, 'Yes', {'Math': 6, 'Biology': 7, 'Economics': 7})
    students = [Obama_student.fullname, Musk_student.fullname, Macron_student.fullname]
    return print(f'Students: {students}\n')


# Obama_person = Person('Barack Obama', 60, 'Yes')
# Obama_person.introduce_myself()
#
# Musk_student = Student('Elon Musk', 50, 'No', {'Math': 9, 'Biology': 8, 'Economics': 9})
# Musk_student.AVG_Rating()
#
# Hanks_teacher = Teacher('Tom Hanks', 65, 'Yes', 8)
# Hanks_teacher.total_salary()

create_student()

