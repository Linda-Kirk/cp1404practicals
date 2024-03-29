"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability=50.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like the parent car but only if reliability > random reliability"""
        distance_driven = 0
        random_float = random.uniform(0.0, 100.0)
        if random_float < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
