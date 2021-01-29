# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('5-2.txt', 'r', encoding='utf-8') as file_obj:
    lines = 0
    for idx, line in enumerate(file_obj, 1):
        lines += 1
        words = 0
        flag = False
        for symbol in line:
            if symbol != ' ' and flag is False:
                words += 1
                flag = True
            elif symbol == ' ':
                flag = False
        print(f'{idx}-я строка -> количество слов: {words}')
    print(f'Количество строк в файле: {lines}')
