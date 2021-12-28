n = int(input('Введіть число: '))
A = [0, 9, 9, 0]
for i in range(3, n+1):
    A[i] = A[i-1] + A[i-2] + A[i-3]
    A.append(A[i])
print('A[{0}]={1}'.format(n, A[n]))
