# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# speed  - атрибут метода
# color - атрибут экземпляра
# name - атрибут экземпляра
# is_police (булево) - атрибут класса
class Car:
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print(f"Машина марки {self.name} поехала со коростью {self.speed} км/ч.")

    def stop(self):
        self.speed = 0
        print(f"Машина марки {self.name} остановилась.")

    def turn(self, direction):
        if direction == "налево" or direction == "направо":
            print(f"Машина марки {self.name} повернула {direction}.")
        else:
            print(f"Чтобы изменить направление движения введите команду 'налево' или 'направо'")

    def show_speed(self):
        print(f'Машина марки {self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость! Допустима скорость до 60 км/ч. Ваша скоростью {self.speed} км/ч.')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена скорость! Допустима скорость до 40 км/ч. Ваша скоростью {self.speed} км/ч.')
        else:
            super().show_speed()


class PoliceCar(Car):
    is_police = True


town_car = TownCar("Mini_Cooper", 'Yellow')
town_car.go(40)
town_car.show_speed()
town_car.turn("направо") # ввести направление "направо" или "налево"
town_car.stop()
sport_car = SportCar("Lamborghini", 'Red')
sport_car.go(180)
sport_car.show_speed()
sport_car.turn("налево") # ввести направление "направо" или "налево"
sport_car.stop()
work_car = WorkCar("Kamaz", "Black")
work_car.go(50)
work_car.show_speed()
work_car.turn("назад") # ввести направление "направо" или "налево"
work_car.stop()
police_car = PoliceCar("BMW", "Whight")
police_car.go(50)
police_car.show_speed()
police_car.turn("налево") # ввести направление "направо" или "налево"
police_car.stop()
print(police_car.is_police)
