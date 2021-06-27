"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        total_cargo = cargo + self.cargo
        if total_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        self.cargo = total_cargo

    def remove_all_cargo(self):
        value = self.cargo
        self.cargo = 0
        return value
        


