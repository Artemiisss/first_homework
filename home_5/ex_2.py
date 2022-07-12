""" Exersice 2
Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів.
"""
#
stroke_1 = input("Enter some text:")
stroke_2 = stroke_1.split()
words = len(stroke_2)
print('Amount words in ur string:', words)
print('Amount elements in ur string', len([i for i in stroke_1 if i.isdigit() + i.isalpha()]))