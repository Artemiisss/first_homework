# exersice 1
_name = input('enter ur name:')
print('Hello,' + _name + '!')


# exersice 2
n = int(input('please enter an integer number:'))
print('the next number for the number', n, 'is', n + 1, '.')
print('the previous number for the number', n, 'is', n - 1, '.')


# exersice 3
speed = int(input('enter the speed:'))
time = int(input('enter the time:'))
distance = speed * time
LENGTH_TRACK = 100
print(distance % LENGTH_TRACK)


# exersice 4
y = int(input('enter a number:'))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("YES")
else:
    print("NO")


# exersice 5
x = int(input('enter a number:'))
if x > 0:
    print('sign(x) = 1')
elif x < 0:
    print(' sign(x) = -1')
else:
    print('sign(x) = 0')


# exersice 6
some_range = tuple(range(10, 101, 10))
x = abs(int(float(input('enter the number u looking for:'))))
if x in some_range:
    print(x)
else:
    print('number is absent')

# exersice 7
x = int(input('enter the number:'))
print('*' * x)
