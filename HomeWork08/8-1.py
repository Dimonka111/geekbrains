'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:
    @classmethod
    def int_date(cls, date):
        date = date.replace('-', '')
        return f'{int(date[:2]):02}.{int(date[2:4]):02}.{int(date[4:])}'

    @staticmethod
    def validating(date):
        try:
            date = date.replace('-', '')
            if int(date[:2]) not in range(1, 32) or int(date[2:4]) not in range(1, 13):
                raise ValueError('ValueError')
            else:
                return f'Допустимый формат даты'
        except ValueError as error:
            print(f'Ошибка {error}: недопустимый формат даты (диапазон дней от 1 до 31, диапазон месяцев от 1 до 12')


print(Date.validating('01-10-1993'))
print(Date.int_date('01-10-1993'))