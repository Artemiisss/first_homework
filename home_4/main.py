""""  Exersice 1
Першого дня спортсмен пробіг `x` кілометрів, а потім він щодня збільшував пробіг на 10% від попереднього

значення. За цим числом `y` визначте номер дня, на який відстань спортсмена складе не менше `y` кілометрів.

Програма отримує на вхід числа `x` та `y` і має вивести одне число - номер дня."""

start_distance = int(input("Enter start distance: "))
end_distance = int(input("Enter end distance: "))
days = 1
while start_distance < end_distance:
    days += 1
    start_distance *= 1.1
print('It will take', days, 'days to cover', end_distance, 'km')

""" Exersice 2 """


def input_number(number: str) -> int:
    result = ''
    while not result.isdigit():
        result = input(number)
    return int(result)


def receiving_amount(sequence: list) -> int:
    return len(sequence)


def receiving_sum(sequence: list) -> int:
    r_sum = 0
    for element in sequence:
        r_sum += element
    return r_sum


def receiving_multiplication(sequence: list) -> int:
    r_mult = 1
    for integers in sequence:
        r_mult *= integers
    return r_mult


def arithmatic_average(sequence: list) -> float:
    ar_avg = (receiving_sum(sequence) / receiving_amount(sequence)) * 10 // 1 / 10
    return ar_avg


def receiving_highest_element(sequence: list) -> tuple:
    highest_num_1 = 0
    index = 0
    for i, elem in enumerate(sequence):
        if highest_num_1 < elem:
            highest_num_1 = elem
            index = i + 1
    return index, highest_num_1


def receiving_even_numbers(sequence: list) -> int:
    count = 0
    for i in sequence:
        if i % 2 == 0:
            count += 1
    return count


def receiving_uneven_numbers(sequence: list) -> int:
    count = 0
    for i in sequence:
        if i % 2 != 0:
            count += 1
    return count


def receiving_second_highest_element(sequence: list, highest_num: int) -> tuple:
    highest_num_2 = 0
    for i in sequence:
        if highest_num_2 < i < highest_num:
            highest_num_2 = i
    return highest_num_2


def receiving_sequence_element(sequence: list, number: int) -> int:
    count = 0
    for i in sequence:
        if i == number:
            count += 1
    return count


def main():
    chain_list = []
    chain = ''
    while chain != 0:
        chain = input_number('Enter a positive numbers,if u want tot stop enter 0: ')
        if chain != 0:
            chain_list.append(chain)
        else:
            highest_elem = receiving_highest_element(chain_list)

    print(f'\nYour entering sequence: {chain_list}')
    print(f'Receiving an amount of elements: {receiving_amount(chain_list)}')
    print(f'Receiving a sum of elements: {receiving_sum(chain_list)}')
    print(f'Receiving a multiplication of elements: {receiving_multiplication(chain_list)}')
    print(f'Receiving a arithmatic average of elements: {arithmatic_average(chain_list)}')
    print(f'Receiving a highest element: {receiving_highest_element(chain_list)[1]}')
    print(f'Receiving highest element with index: {receiving_highest_element(chain_list)[0]}')
    print(f'Receiving an even numbers: {receiving_even_numbers(chain_list)}')
    print(f'Receiving an uneven numbers: {receiving_uneven_numbers(chain_list)}')
    print(f'Receiving a second highest number: {receiving_second_highest_element(chain_list, highest_elem[1])}')
    print(
        f'Receiving sequence elements which are equal highest : {receiving_sequence_element(chain_list, highest_elem[1])}')


if __name__ == '__main__':
    main()

""" Exersice 3
 Дано два цілих числа 'A' і 'В'. Виведіть усі числа від `A` до `B` включно, в порядку зростання,
  якщо `A < B`, або в порядку зменшення в іншому випадку.
"""
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
if first_number < second_number:
    for i in range(first_number, second_number + 1, 1):
        print(i, end=",")
else:
    for i in range(first_number, second_number - 1, -1):
        print(i, end=",")

""" Exersice 4 """


def up_stairs(start: int, end=9):
    stairs_step = ''
    for num in range(start, end + 1):
        stairs_step += str(num)
        print(stairs_step)


def main():
    up_stairs(1, 9)


if __name__ == "__main__":
    main()

""" Exersice 5 """


def entering_string():
    _string = input('Enter your row:')
    return str(_string)


def main():
    _string = entering_string()
    print(f'\nThis is your raw: {_string}')
    print(f'The third element in your raw: {_string[2]}')
    print(f'The penultimate element in your raw: {_string[-2]}')
    print(f'The first five element in your raw: {_string[0:5]}')
    print(f'The whole raw without two last elements: {_string[0:-2]}')
    print(f'The elements with paired index: {_string[0::2]}')
    print(f'The element without paired index: {_string[1::2]}')
    print(f'The reversed raw: {_string[::-1]}')
    print(f'The reversed raw with every second element: {_string[-1::-2]}')
    print(f'The length of your raw: {len(_string)}')


if __name__ == "__main__":
    main()

""" Exersice 6 """

list_of_numbers = (input('Enter your list of numbers:'))
count = 0
for i, _ in enumerate(list_of_numbers):
    if 0 < i < len(list_of_numbers) - 1 and list_of_numbers[i - 1] < list_of_numbers[i] > list_of_numbers[i + 1]:
        count += 1

print('\nYour list:', list_of_numbers)
print('Amount of elements which are larger than their neighbors:', count)

""" Exersice 7 """

first_list = input('Enter first list of numbers:')
second_list = input('Enter second list of numbers:')

first_set = set(first_list)
second_set = set(second_list)

print(f'\nNumbers that are in first n second list:{first_set & second_set}')
print(f'Numbers that are in first list but absent in second list: {first_set.difference(second_set)}')
print(f'Unique numbers that are in each list:\n{first_set.difference(second_set)}\n'
      f'{second_set.difference(first_set)}')
