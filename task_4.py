"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Поворачиваем {direction}')

    def show_speed(self):
        print(f'Скорость = {self.speed}')


class TownCar(Car):
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость! Ваша скорость = {self.speed} км/ч')
        else:
            print(f'Скорость = {self.speed}')


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
            print(f'Превышена скорость! Ваша скорость = {self.speed} км/ч')
        else:
            print(f'Скорость = {self.speed}')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


car = Car(50, 'белый', 'Kia', False)
car.show_speed()
car.stop()

car1 = TownCar('коричневый', 'Nissan')
car1.go(80)
car1.show_speed()

car2 = WorkCar('красный', 'Lada')
car2.go(35)
car2.show_speed()

police = PoliceCar('чёрный', 'BMV')
print(police.is_police)
