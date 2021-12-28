import random
n = int(input("Кількість рядків та стовпців: "))
matrix = [[(random.randint(-10,10)) for j in range(n)] for i in range(n)]
vec = [(random.randint(-10,10)) for i in range(n)]
for i in range(n):
    matrix[i] = list(map(lambda x, y: x * y, matrix[i], vec))
print(*matrix, sep = "\n")
