import math
x1 = float(input('Введіть х1: '))
y1 = float(input('Введіть y1: '))
x2 = float(input('Введіть х2: '))
y2 = float(input('Введіть y2: '))
cos = ((x1 * x2) + (y1 * y2))/(math.sqrt(x1**2+y1**2)*(math.sqrt(x2**2+y2**2)))
print('cos= {0:.2f}'.format(cos))
