"""To the GroundVehicle class, add method drive() that returns "vroooom".

Also change it so the num_wheels defaults to 4 if not specified when the
object is constructed."""
from collections import namedtuple

Engine = namedtuple("Engine", "style sound")
V6 = Engine("6-cylinder", "vroooom")
Twin = Engine("Twin-cylinder", "BRAAAP!!")


class GroundVehicle:
    # We can set our defaults as class attributes here
    num_wheels = 4
    engine = V6

    def __new__(cls, *args, **kwargs):
        """Using the new method to check for subclassing"""
        if cls.__name__ == 'Motorcycle':
            cls.engine = Twin
            cls.num_wheels = 2
        return super().__new__(cls)

    @property  # Then we can define a class property to return the attribute noise
    def drive(self):
        return self.engine.sound


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    pass


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]
