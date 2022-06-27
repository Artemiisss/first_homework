""" Exersice 1
Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000, і повертає `True`,
 якщо воно просте, і `False` - інакше.
(Прості числа - ті які діляться без залишку тільки на себе або 1, наприклад 2, 3, 5, 7, 11 ...)
"""


def is_prime(number):
    if n in range(0, 1001):
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


while True:
    n = -1
    while n not in range(0, 1001):
        n = int(input("Enter number between 1 and 1000:"))
    print(is_prime(n))
    a = input("Continue???  1 - No, Eny Key - Yes")
    try:
        if int(a) == 1:
            break
    except:
        ValueError

""" Exersice 2 
Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів.
"""
#
stroke_1 = input("Enter some text:")
stroke_2 = stroke_1.split()
words = len(stroke_2)
print('Amount words in ur string:', words)
print('Amount elements in ur string', len([i for i in stroke_1 if i.isdigit() + i.isalpha()]))

""" Exersice 3
 Написати функцію яка поверне площу фігури: за замовчуванням трикутника, опціонально квадрату. 
 На вході 2 величини та параметр типу фігури
 """

type_of_figure = str(input("Enter the name of figure:"))
if type_of_figure == "triangle":
    first_side = float(input("Entering side а = "))
    second_side = float(input("Entering side b = "))
    area = ((first_side * second_side) / 2)
    print("Figure area:", area)
elif type_of_figure == "square":
    sq_side = float(input("Entering side = "))
    area = sq_side ** 2
    print("Figure area:", area)
else:
    print("Wrong type")

""" Exersuce 4
Даний перелік випадкових цілих чисел. Замініть усі непарні числа списку нулями. І виведете їхню кількість
"""
string = list(range(1, 11, 1))
for n, i in enumerate(string):
    if i % 2 != 0:
        string[n] = 0
count = string.count(0)
print("Odds numbers were swiped to zero:", string)
print("Amount of odds in ur list = ", count)

""" Exersice 5
 Написати функцію square, що приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
  периметр квадрата, площа квадрата та діагональ квадрата.
  """

a = int(float(input('Enter side of square: ')))


def square(side: int):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * 2 ** 0.5
    return [perimeter, area, round(diagonal, 2)]


print(square(a))

""" Exersice 6
Написати функцію яка прибере з dict елементи із значеннями None
"""
some_dict = {'Mercedes': 'SLS', 'BMW': 'i8', 'Alfa-romeo': None, 'Koenigsegg': 'Agera R', 'Nissan': 'Teana',
             'Audi': None}
print(some_dict)
some_dict = {k: v for k, v in some_dict.items() if v is not None}
print(some_dict)

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
