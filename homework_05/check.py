from homework_05.exceptions import CargoOverload
from homework_05.car import Car
from homework_05.plane import Plane

#Проверка кода

def main():
    car = Car(weight=1000, fuel=10, fuel_consumption=1)
    car.start()
    car.move(5)
    print(car.fuel)  

    plane = Plane(weight=1000, fuel=100, fuel_consumption=2, max_cargo=50)
    plane.load_cargo(30)
    try:
        plane.load_cargo(25)
    except CargoOverload:
        print("Перегружен авто")

    print(plane.remove_all_cargo())  
    print(plane.cargo)          

    
if __name__ == "__main__":
    main()