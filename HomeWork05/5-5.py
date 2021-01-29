# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5-5.txt', 'w') as file_obj:
    user_enter = input('Ввод чисел, разделенных пробелом: ').split(' ')
    file_obj.write(' '.join(user_enter))

with open('5-5.txt', 'r') as file_obj:
    for line in file_obj:
        line_list = line.split(' ')
        int_line_list = [int(el) for el in line_list]
    print(f'Сумма чисел: {sum(int_line_list)}')