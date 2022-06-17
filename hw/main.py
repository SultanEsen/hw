from cars.create_car import create_car
from cars.get_car_info import get_car_info

bmw = create_car('BMW', 'X7', 2020, 5, 20000)
bmw.start()
bmw.stop()

mers = get_car_info('Mers', 'W140', 1995, 6, 500000)