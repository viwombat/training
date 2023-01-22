"""
Implement a class that describes an engine object.
During instance creation we should set model_name, number_of_cylinders,
engine_displacement, engine_resource (will count in kilometers), fuel_type.
Implement a method that represent engine information.
Add description at docstring.
"""


class Engine:

    def __init__(self,
                 model_name: str,
                 number_of_cylinders: int,
                 engine_displacement: float,
                 engine_resource: float,
                 fuel_type: str) -> None:

        self.model_name = model_name
        self.number_of_cylinders = number_of_cylinders
        self.engine_displacement = engine_displacement
        self.engine_resource = engine_resource
        self.fuel_type = fuel_type

    def __repr__(self) -> None:
        """The description of an engine"""

        print(f'The model is"{self.model_name}" model. The Engine has {self.number_of_cylinders} cylinders, ' 
              f'{self.engine_displacement} engine_displacement, resource is {self.engine_resource} km, ' 
              f'fuel type: "{self.fuel_type}"')
