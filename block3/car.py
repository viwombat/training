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
import copy
from datetime import date
from random import random
from typing import Union

from modern_engine import ModernEngine
from engine import Engine


class Car:

    def __init__(self,
                 brand: str,
                 car_type: str,
                 color: str,
                 engine: Union[Engine, ModernEngine],
                 year: str,
                 month: str) -> None:

        self.brand = brand
        self.car_type = car_type
        self.color = color
        self.engine = engine
        self.year = year
        self.month = month

    def vin_generator(self) -> str:
        return f"{self.car_type[0]}-{self.color[0]}-{self.year}-{self.month}-{self.engine.unique_number}"

    # @classmethod
    # def rename_brand(cls, new_name) -> None:
    #     cls.brand = new_name

    @staticmethod
    def some_static_method() -> date:
        return date.today()

    def __str__(self) -> None:
        """The description of a car"""
        print(f'Car "{self.brand}". '
              f'(Vin code: {self.vin_generator()} - '
              f'{self.car_type}, {self.color}, {self.brand}, {self.engine.model_name})')


engine1 = Engine("model1", 2, 40, 5, "5")
engine2 = Engine("model2", 3, 50, 10, "2")
engine4 = ModernEngine("model4", 4, 60, 15, "1", 100)

car = Car("Audi", "some_car_type", "blue", copy.deepcopy(engine1), "2020", "05")

engine1.model_name = "modelmodel"

print(engine1.model_name)
print(car.engine.model_name)
