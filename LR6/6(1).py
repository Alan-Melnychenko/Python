import random
n = random.randint(0, 100)
a = []
min = -100
for i in range(n):
    a.append(random.randint(-100, 100))
print(a)
for i in range(n):
    if a[i] < 0:
        if a[i] > min:
            min = a[i]
print("Найбільше серед від'ємних = {0}".format(min) )
