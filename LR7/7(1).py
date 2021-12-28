import random
sum = 0
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[(random.randint(-10,10)) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2==0 and a[i][j]<0:
            sum+=a[i][j]
print(*a,sep='\n')
print('sum={0}'.format(sum))
