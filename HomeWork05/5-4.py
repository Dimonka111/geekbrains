# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('5-4(en).txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        for key in numbers.keys():
            line = line.replace(key, numbers[key])
        with open('5-4(ru).txt', 'a', encoding='utf-8') as second_file_obj:
            print(line, file=second_file_obj)