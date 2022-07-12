""" Exersice 5
 Написати функцію square, що приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
  периметр квадрата, площа квадрата та діагональ квадрата.
  """

a = int(float(input('Enter side of square: ')))


def square(side: int):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * 2 ** 0.5
    return perimeter, area, round(diagonal, 2)


print(square(a))