'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a}+{self.b}j)'

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


first = ComplexNumber(1, 4)
second = ComplexNumber(2, 5)
print(f'Первое компексное число: {first}')
print(f'Второе комплексное число: {second}')
print(f'Результат сложения комплексных чисел: {first + second}')
print(f'Результат умножения комплексных чисел: {first * second}')