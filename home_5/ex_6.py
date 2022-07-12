""" Exersice 6
Написати функцію яка прибере з dict елементи із значеннями None
"""
some_dict = {'Mercedes': 'SLS', 'BMW': 'i8', 'Alfa-romeo': None, 'Koenigsegg': 'Agera R', 'Nissan': 'Teana',
             'Audi': None}
print(some_dict)
some_dict = {k: v for k, v in some_dict.items() if v is not None}
print(some_dict)