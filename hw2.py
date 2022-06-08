class Company:
    def __init__(self, company_name, company_bank):
        self.company_name = company_name
        self.company_bank = company_bank


class Person(Company):
    def __init__(self, company_name, company_bank, first_name, last_name, salary):
        super().__init__(company_name, company_bank)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.salary > self.company_bank:
            print(f'The {self.company_name} company does not have enough funds!”')
        else:
            self.company_bank -= self.salary
            print(f'{self.first_name} {self.last_name} received salary of {self.salary} USD\n'
                  f'Current balance of {self.company_name}: {self.company_bank}')

    def person_info(self):
        print(f'First name: {self.first_name}\nLast name: {self.last_name}\nSalary: {self.salary} USD\n')


person1 = Person('IBM', 1000000, 'Tom', 'Hanks', 10000)
person1.person_info()
person1.get_salary()
person1.get_salary()
person1.get_salary()