from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel;
        self.fuel_consumption = fuel_consumption;
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                return 
            raise exceptions.LowFuelError

        print("Already started")

    def move(self, distance):
        total_consumption = self.fuel_consumption * distance
        if self.fuel < total_consumption:
            raise exceptions.NotEnoughFuel
        self.fuel -= total_consumption
        print(f"move {distance} km; fuel: {self.fuel}")
            
