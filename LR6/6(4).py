import random
a = int(input('Введіть число: '))
b = int(input('Введіть число: '))
m = []
n = random.randint(0, 10)
for x in range(n):
    m.append(random.randint(-10, 10))
print(m)
i = 0
for x in m:
    if a <= abs(x) <= b:
        m.pop(i)
    i += 1
print(m)
