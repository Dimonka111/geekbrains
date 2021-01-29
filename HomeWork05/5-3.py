# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('5-3.txt', 'r', encoding='utf-8') as f_obj:
    data_base = []
    for line in f_obj:
        line_list = line.split(' ')
        line_list[1] = float(line_list[1][:-1])
        data_base.append(line_list)
    data_dict = dict(data_base)
    incomes = [values for keys, values in data_dict.items()]
    middle_income = round(sum(incomes) / len(incomes), 2)
    print(f'Средняя величина оклада сотрудников: {middle_income} руб.')
    print('Сотрудники с окладом менее 20 тыс. руб.: ')
    for key, value in data_dict.items():
        if value < 20000:
            print(f'{key}: {value} руб.')
