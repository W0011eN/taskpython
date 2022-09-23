#Задание 4
#Реализуйте базовый класс Car.
#    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police 
        
    def go (self,speed):
        self.speed=speed
        print(f'Увеличиваем скрость до {speed} км\ч')
        
    def stop (self):
            self.speed=0
            print("Скорость равна 0 км\ч")
        
    def turn (self,direction):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')
        
    def show_speed (self):
        print(f'Ваша скорость {self.speed} км/ч\n')
    
class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
    
    def show_speed (self):
        if self.speed > 60:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Ваша скорость {self.speed} км/ч\n')

class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def driveCar(mashine):
    print(f"Автомобиль {mashine.name}, цвет {mashine.color}")
    mashine.go(40)
    mashine.show_speed()
    mashine.turn('направо')
    mashine.stop()
    mashine.show_speed()
    mashine.turn('налево')
    mashine.go(60)
    mashine.show_speed()
    mashine.go(120)
    mashine.show_speed()
    mashine.stop()

car = TownCar('белый', 'УАЗ')
driveCar(car)
car = WorkCar('черный', 'БелАЗ')
driveCar(car)
car = PoliceCar('синий', 'Волга')
driveCar(car)
