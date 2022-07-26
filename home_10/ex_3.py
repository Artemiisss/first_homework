"""Написати функцію яка зрушить отриманий список на N елементів вправо або вліво, аргументи,
що приймаються - список і натуральне число(якщо негативне зрушуємо вліво, позитивне - вправо)."""

some_list = [1, 2, 3, 4, 5, 6, 7, 8]


def shifted_elements(roster, shift=0):
    run = len(roster)
    for i, ele in enumerate(roster[:]):
        roster[(i + shift) % run] = ele
    return roster


print(some_list)
shifted_elements(some_list, 2)
print(some_list)
shifted_elements(some_list, -4)
print(some_list)
