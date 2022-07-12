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