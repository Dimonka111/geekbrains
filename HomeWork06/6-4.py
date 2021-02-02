'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'Автомобиль: марка - {self.name}; цвет - {self.color}')
        if self.is_police:
            print('Полицейский автомобиль')
        else:
            print('Штатский автомобиль')

    def go(self):
        print(f'Автомобиль {self.name} (цвет {self.color}) поехал')

    def stop(self):
        print(f'Автомобиль {self.name} (цвет {self.color}) остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} (цвет {self.color}) повернул на {self.direction}')

    def show_speed(self):
        print(f'Автомобиль {self.name} (цвет {self.color}). Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} (цвет {self.color}). Скорость {self.speed}: превышение скорости!')
        else:
            print(f'Автомобиль {self.name} (цвет {self.color}). Скорость {self.speed}: в допустимых пределах')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} (цвет {self.color}). Скорость {self.speed}: превышение скорости!')
        else:
            print(f'Автомобиль {self.name} (цвет {self.color}). Скорость {self.speed}: в допустимых пределах')


class PoliceCar(Car):
    pass


city_auto = TownCar('Toyota Corolla', 59, 'серый', False)
fast_auto = SportCar('Ferrari F-40', 167, 'красный', False)
job_auto = WorkCar('Hyundai Solaris', 53, 'синий', False)
police_auto = PoliceCar('Ford Focus', 102, 'белый', True)

city_auto.go()
fast_auto.go()
job_auto.go()
police_auto.go()

city_auto.stop()
fast_auto.stop()
job_auto.stop()
police_auto.stop()

city_auto.turn('Юг')
fast_auto.turn('Север')
job_auto.turn('Восток')
police_auto.turn('Запад')

city_auto.show_speed()
fast_auto.show_speed()
job_auto.show_speed()
police_auto.show_speed()