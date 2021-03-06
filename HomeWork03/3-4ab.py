# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый способ

def my_func_1(x, y):
    return x ** y


print(my_func_1(10, -2))


# Второй способ

def my_func_2(x, y):
    otvet = 1
    if y >= 0:
        while y != 0:
            otvet *= x
            y -= 1
    else:
        while y != 0:
            otvet /= x
            y += 1
    return otvet


print(my_func_2(10, -2))
