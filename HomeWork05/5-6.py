# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('5-6.txt', 'r', encoding='utf-8') as file_obj:
    symbols = [':', '(л)', '—', '(пр)', '(лаб)', '\n']
    list_of_lessons = []
    for line in file_obj:
        for i in symbols:
            line = line.replace(i, '')
        line_list = line.split(' ')
        for el in line_list:
            if el == '':
                line_list.remove(el)
        line_list_lessons = [int(el) for el in line_list[1:]]
        lesson_info = [line_list[0], sum(line_list_lessons)]
        list_of_lessons.append(lesson_info)
    dict_of_lessons = dict(list_of_lessons)
    print(dict_of_lessons)