'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''

income_stats = {'wage': {'builder': 25000, 'foreman': 30000}, 'bonus': {'builder': 10000, 'foreman': 15000}}


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return income_stats.get('wage').get(self.position) + income_stats.get('bonus').get(self.position)


first_worker = Position('Ivan', 'Krylov', 'builder', income_stats)
print(f'Полное имя: {first_worker.get_full_name()}')
print(f'Доход с учетом премии: {first_worker.get_total_income()} руб.')
second_worker = Position('Anton', 'Evseev', 'foreman', income_stats)
print(f'Полное имя: {second_worker.get_full_name()}')
print(f'Доход с учетом премии: {second_worker.get_total_income()} руб.')
