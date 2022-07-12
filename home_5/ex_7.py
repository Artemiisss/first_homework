""" Exersice 7
дод. Написати функцію `is_date`, що приймає 3 аргументи - день, місяць і рік.
Повернути `True`, якщо дата коректна (треба враховувати число місяця.
Наприклад 30.02 - дата не коректна, так само 31.06 або 32.07 тощо), та `False` інакше.
"""


def date(day, month, year):
    if day <= 0 or month <= 0 or year < 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0:  months[1] = 29
        if day <= months[month - 1]:
            if month <= 12:
                return True
        return False


if __name__ == '__main__':
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))
    print(date(day, month, year))