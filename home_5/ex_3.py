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