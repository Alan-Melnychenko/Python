import random
n = int(input('Введіть розмірність матриці: '))
for i in range(n):
    for j in range(n):
        a = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
list = []
for el in a[1::2]:
    b = [sorted(el, reverse=True)]
    list += b
a[1::2] = list
print(*a, sep= '\n')
