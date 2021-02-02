'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
'''
from time import sleep


class TrafficLight:
    __color = 'red'

    @staticmethod
    def running(color):
        if color == 'red':
            while True:
                print(f'Now works {color}')
                sleep(7)
                color = 'yellow'
                print(f'Now works {color}')
                sleep(2)
                color = 'green'
                print(f'Now works {color}')
                sleep(12)
                color = 'red'
        if color == 'yellow':
            while True:
                print(f'Now works {color}')
                sleep(2)
                color = 'green'
                print(f'Now works {color}')
                sleep(12)
                color = 'red'
                print(f'Now works {color}')
                sleep(7)
                color = 'yellow'
        if color == 'green':
            while True:
                print(f'Now works {color}')
                sleep(12)
                color = 'red'
                print(f'Now works {color}')
                sleep(7)
                color = 'yellow'
                print(f'Now works {color}')
                sleep(2)
                color = 'green'


light_time = TrafficLight()
light_time.running(light_time._TrafficLight__color)
