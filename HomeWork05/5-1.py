# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_obj = open('5-1.txt', 'a', encoding='utf-8')
while True:
    user_enter = input('Введите текст (для выхода оставьте строку пустую и нажмите "Enter": ')
    if user_enter == '':
        break
    file_obj.write(user_enter + '\n')
file_obj.close()
print(f'Конец записи в файл {file_obj.name}')

