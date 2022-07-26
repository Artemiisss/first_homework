"""1. Програма яка при запуску повинна:
Створити текстовий файл, записати в нього дані, які вводить користувач.
Закінченням введення нехай служить порожній текст. Кожен введений текст у файлі повинен починатися з нового рядка."""


with open('home_10.txt', 'wt') as file:
    while True:
        text = input('Write smth down, but if u wanna stop, press "enter":')
        file.write(text + '\n')
        if text == '':
            break
# file.close()
# file.read()
# print(file.readline())

