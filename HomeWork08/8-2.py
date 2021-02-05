'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


input_dividend = int(input('Введите делимое: '))
input_divider = int(input('Введите делитель: '))
try:
    if input_divider == 0:
        raise DivisionByZero('Деление на ноль невозможно!')
except DivisionByZero as error:
    print(f'{error}')
else:
    print(f'Частное: {input_dividend / input_divider}')