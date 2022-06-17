from .models import Car
import os

def get_car_info(title, model, year, engine, miles):
    # new_car = Car(title=title, model=model, year=year, engine=engine, miles=miles)
    print(f'''Car info:
Title: {title}
model: {model}
year: {year}
engine: {engine}
miles: {miles}

''' )
