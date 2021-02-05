'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''


class NotInt(ValueError):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    user_input = input('Введите очередной элемент списка: ')
    if user_input == 'stop':
        print('Конец программы')
        break
    try:
        user_input = int(user_input)
        if type(user_input) == int:
            user_list.append(user_input)
        else:
            raise NotInt('ошибка')
    except ValueError as NotInt:
        print(f'Ошибка, список принимает только числа')

print(f'Итоговый список: {user_list}')