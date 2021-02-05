# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности
# реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class StorageElectronics:
    def __init__(self, name):
        self.name = name
        self.count_el = []

    def __str__(self):
        res = f'\nИтого {self.name}:\n'
        if self.count_el:
            for i, item in enumerate(self.count_el, 1):
                res += f'{i}: {item}\n'
        else:
            res += 'ничего нет!'
        return res

    def income(self, eqpt_el):
        self.count_el.append(eqpt_el)


class Electronics:
    def __init__(self, qty, brand, price):
        self.brand = brand
        self.qty = qty
        self.price = price

    def __str__(self):
        return f'{self.type_name} {self.brand} стоимость: {self.price}$ в наличии: {self.qty} шт.'


class Printer(Electronics):
        type_name = 'Принтер'


class Scanner(Electronics):
        type_name  = 'Сканнер'


class Xerox(Electronics):
        type_name = 'Ксерокс'


r = Printer(price=130, brand='HP', qty=3)
print(r)

a = Scanner(qty=4, price=100, brand='Canon')
print(a)

x = Xerox(qty=1, price=89, brand='Xerox')
print(x)

list_storage = StorageElectronics('Склад Мск')

list_storage.income(r)
list_storage.income(a)
list_storage.income(x)
print(list_storage)

list_storage_2 = StorageElectronics('Склад Питер')
list_storage_2.income(x)
print(list_storage_2)