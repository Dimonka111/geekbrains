'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        copy_data = []
        for el in self.input_data:
            el = ' '.join(str(num) for num in el)
            copy_data.append(el)
        copy_data = '\n'.join(str(el) for el in copy_data)
        return copy_data

    def __add__(self, other):
        element_of_result = []
        result = []
        for i in range(len(self.input_data)):
            for j in range(len(self.input_data[i])):
                plus = self.input_data[i][j] + other.input_data[i][j]
                element_of_result.append(plus)
                if len(element_of_result) == len(self.input_data[j]):
                    result.append(element_of_result)
                    element_of_result = []
        return Matrix(result)


first_array = Matrix([[2, 3, 5], [0, -2, 4], [9, 1, -5]])
second_array = Matrix([[1, 4, 8], [6, 3, 7], [5, 0, -2]])
print(first_array, '\n')
print(second_array, '\n')
print(first_array + second_array)