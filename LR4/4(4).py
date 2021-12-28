import math
x = float(input('Введіть перше число: '))
y = float(input('Введіть друге число: '))
z = 0
if y < x:
    z = y * math.e ** x
elif y > x:
    z = x * math.e ** y
else:
    z = y * x
print('Число z={0:.2f}'.format(z))
