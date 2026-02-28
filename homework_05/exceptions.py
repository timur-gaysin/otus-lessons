"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    """Вызывается когда авто запускается с низкм количеством топлива """
    pass

    
class NotEnoughFuel(Exception):
    """Вызывается при попытке перемещения авто без топлива"""
    pass
    
class CargoOverload(Exception):
    """Вызываетсякогда пытаемся загрузить Карго сверх лимита"""
    pass
