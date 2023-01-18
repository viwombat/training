"""
Create a class that extends engine class. The class has additional instance attributes such as current_engine_mileage,
unique number. For each instance you should generate unique number (think how to do it). Create a method that
takes number of kilometers and increases current engine mileage. Also we need a property that shows how many
engine resource an engine has if we know the current engine mileage of a car.
"""

import itertools
from engine import Engine


class ModernEngine(Engine):

    unique_number = itertools.count()

    def __init__(self, model_name,
                 number_of_cylinders,
                 engine_displacement,
                 engine_resource,
                 fuel_type,
                 current_engine_mileage):
        super().__init__(model_name, number_of_cylinders, engine_displacement, engine_resource, fuel_type)

        self.unique_number = next(ModernEngine.unique_number)
        self.current_engine_mileage = current_engine_mileage

    def increase_miles(self, kilometers):
        self.current_engine_mileage += kilometers
        return self.current_engine_mileage

    def current_engine_resource(self):
        self.engine_resource -= self.current_engine_mileage
        return self.engine_resource
