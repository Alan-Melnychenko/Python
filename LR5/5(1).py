import math
a = 4
for i in range(1, 13):
    a = a - math.cos(a**i/12)
print('a(12)={0:.2f}'.format(a))
