import random
import math
n = random.randint(1, 10)
x = random.randint(-10, 10)
A = []
B = []
a = 0
dob = 1
sum = 0
b = 0
for i in range(n):
    a = ((i-1)**2)/(2*i**2-1)+math.factorial(i) * math.sin(i*x)
    A.append(a)
    if a < 0:
        b = a * dob
        dob *= a
        B.append(b)
    else:
        b = abs(a) + sum
        sum += i*abs(a)
        B.append(b)
print('Множина А = {0}'.format(A))
print('Множина B = {0}'.format(B))
