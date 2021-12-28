import random
n = int(input("Кількість рядків та стовпців: "))
a = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
matrix = [[0] * n for i in range(n)]
for j in range(n):
    for i in range(n):
        matrix[j][i] = a[i][j]
collumn = 0
for el in matrix:
    count = 0
    m = list(filter(lambda x: x < 0, el))
    if len(m) > 0:
        collumn += 1
        continue
    else:
        collumn += 1
        count = sum(el)
    print("Сума чисел стовпця № {0}: {1}".format(collumn, count))
print(*a, sep = '\n')
