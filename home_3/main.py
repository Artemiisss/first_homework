from random import randint

"""" Exersice 1"""
_number = int(input('Enter number of three:'))
print(_number // 100 + ((_number // 10) % 10) + _number % 10)

"""" Exersice 2"""
x = float(input('Enter a number with floating point:'))
print(int(x % 1 * 100))
print(int(x % 1 * 10))

""" Exersice 3"""
list_ten = [10, 20, 30, 40, 50]
list_ten.reverse()
print(list_ten)
#
""" Exersice 4"""
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for i in list_of_six:
    if i % 5 == 0 and i < 150:
        print(i)

""" Exersice 5"""
count = 0
guess_number = randint(1, 10)
print(guess_number)
while count < 3:
    x = int(input('Enter a number from 1 to 10: '))
    if x == guess_number:
        print('U won')
        break
    else:
        print('U lose,try again:')
        count += 1

""" Exersice 6"""
x1 = int(input('enter the horizontally cell:'))
y1 = int(input('enter the first vertically cell:'))
y2 = int(input('enter the second vertically cell:'))
dx = abs(x1)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dy == 1:
    print('YES')
else:
    print('NO')

""" Exersice 7"""
n = int(input('Enter a number:'))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print('Factorial of ur number is:', factorial)
