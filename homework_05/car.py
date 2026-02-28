"""
Создайте класс `Car`, наследник `Vehicle`
"""
from typing import Optional

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    engine: Optional[Engine] = None
    
    def set_engine(self, engine: Engine) -> None:
        self.engine = engine