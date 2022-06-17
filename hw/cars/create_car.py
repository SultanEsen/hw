from .models import Car
import os

def create_car(title, model, year, engine, miles):

    car = Car(title=title, model=model, year=year, engine=engine, miles=miles)
    return car

# print(create_car('BMW', 'X7', 2020, 5, 20000))
