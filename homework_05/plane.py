"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.exceptions import CargoOverload
from homework_05.base import Vehicle


class Plane(Vehicle):
    cargo : float
    max_cargo : float = 0.0

    def __init__(self, weight : float = 0.0, fuel: float = 0.0, fuel_consumption: float = 0.0, max_cargo : float = 0.0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0.0

    def load_cargo(self, cargo:float):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload("Грузовик переполнен")
        self.cargo += cargo

    def remove_all_cargo(self) -> float:
        old = self.cargo
        self.cargo = 0.0
        return old
    

    