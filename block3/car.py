'''
Implement a Car class.
Each instance has a type (types examples: Wagon, Sedan, Hatchback, Coupe), model, vin_code, color
(Red, Black, White, Gray, Silver), brand, engine, year, month.
vin code generates as A-B-CCCC-MM-EEEEEEE, where A is the first letter of type, B - first letter of the color,
CCCC - year, MM - month, EEEEEEE - unique number.
Brand is the class attribute. Engine instance pass as an attribute.
*Create one classmethod, one staticmethod for the Car class with any useful logic.

Update the string representation of the Car class to
"Car <brand> (Vin code: <vin_code>) - <type>, <color>, <engine.model_name>, <engine.fuel_type>."
'''

from datetime import date
from random import random

from modern_engine import ModernEngine
from engine import Engine


class Car:

    __brand = "some_brand"

    def __init__(self, car_type, color, engine, year, month):

        self.car_type = car_type
        self.color = color
        self.engine = engine
        self.year = year
        self.month = month

    def vin_generator(self):
        unique_num = str(int(random() * 1000000))
        vin_code = self.car_type[0] + '-' + self.color[0] + '-' + self.year + '-' + self.month + '-' + unique_num
        return vin_code

    @classmethod
    def rename_brand(cls, new_name):
        cls._brand = new_name

    @staticmethod
    def some_static_method():
        current_day = date.today()
        return current_day

    def __str__(self):
        """The description of a car"""
        print(f'Car "{self.__brand}". '
              f'(Vin code: {self.vin_generator()} - '
              f'{self.car_type}, {self.color}, {self.__brand}, {self.engine.model_name})')


engine1 = Engine("model1", "2cyl", 40, 5, 10000)
engine2 = Engine("model2", "3cyl", 50, 10, 5000)
engine4 = ModernEngine("model4", "4cyl", 60, 15, 1000, 100)
