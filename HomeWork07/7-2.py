'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def consumption(self, *args, **kwargs):
        pass

    def __str__(self, *args, **kwargs):
        return self.title

    def __add__(self, other):
        return sum(self.consumption(), other.consumption())


class Coat(Clothes):
    def consumption(self, v):
        result = round(v / 6.5 + 0.5, 2)
        return result


class Suit(Clothes):
    def consumption(self, h):
        result = round(2 * h + 0.3, 2)
        return result


outfit = Coat('Benetton')
outfit_2 = Suit('Hugo Boss')
print(f'Пальто {outfit}')
print(f'Расход ткани - {outfit.consumption(12)}')
print(f'Костюм {outfit_2}')
print(f'Расход ткани - {outfit_2.consumption(4)}')
print(f'Общий расход ткани - {outfit.consumption(12) + outfit_2.consumption(4)}')