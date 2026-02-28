"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError,NotEnoughFuel


class Vehicle(ABC):
    weight : float = 0.0
    started: bool = False
    fuel : float  = 0.0
    fuel_consumption : float  = 0.0

    def __init__(self, weight: float = 0.0, fuel: float = 0.0, fuel_consumption: float = 0.0) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self) -> None:
        if self.started:
            return
        if self.fuel <= 0:
            raise LowFuelError("Ошибка запуска, бензин на нуле")
        
        self.started = True

    def move(self, distance: float) -> None:
        required = distance * self.fuel_consumption
        if(required > self.fuel):
            raise NotEnoughFuel("Недостаточно топлива для перемещения авто")
        self.fuel -= required


    