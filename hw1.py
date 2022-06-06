class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} engine started\n')

    def stop_engine(self):
        print(f'{self.title} {self.model} engine stopped\n')

    def info(self):
        print(f'Title: {self.title}\nModel: {self.model}\nWeight: {self.weight}\nHp: {self.hp}\nNm: {self.nm}\n'
              f'Max_speed: {self.max_speed}\nColor: {self.color}\n')


class BMW(Car):
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        super().__init__(title, model, weight, hp, nm, max_speed, color)

class Mercedes(Car):
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        super().__init__(title, model, weight, hp, nm, max_speed, color)


BMW = BMW('BMW', 'E38', 1856, 286, 440, 250, 'black')
BMW.start_engine()
BMW.info()

Mercedes = Mercedes('Mercedes', 'W140', 2150, 394, 570, 250, 'silver')
Mercedes.start_engine()
Mercedes.info()