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