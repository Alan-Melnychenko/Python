n = int(input("Введіть розмірність матриці : "))
A = [[0 for j in range(n)] for i in range (n)]
B = [1 for i in range(n)]
max = 0
for i in range(n):
    for j in range (n):
        if ((i+1)+(j+1))%2 == 0:
            for g in range(1,i+2):
                A[i][j] += g
        else:
            for g in range(1,j+2):
                A[i][j] += g**2
for j in range(n):
    for i in range(n):
        B[j] *= A[i][j]
    if B[j] % 2 == 0 and B[j] > max:
        max = B[j]
print(*A, sep = "\n")
print('sum_max = {0}\n'.format(max))
