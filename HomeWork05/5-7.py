# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('5-7.txt', 'r', encoding='utf-8') as file_obj:
    sum_firm_profits = []
    firms_data = []
    for line in file_obj:
        line = line.replace('\n', '')
        firm = line.split(' ')
        firm[0] = firm[1] + ' ' + firm[0]
        firm.remove(firm[1])
        firm_params = [int(el) for el in firm[1:]]
        firm_profits = firm_params[0] - firm_params[1]
        firm_info = [firm[0], firm_profits]
        firms_data.append(firm_info)
        if firm_profits >= 0:
            sum_firm_profits.append(firm_profits)
    average_profit = sum(sum_firm_profits) / len(sum_firm_profits)
    dict_average_profit = {'average_profit': average_profit}
    dict_firms_data = dict(firms_data)
    data_base = [dict_firms_data, dict_average_profit]

with open('5-7.json', 'w') as write_f:
    json.dump(data_base, write_f)