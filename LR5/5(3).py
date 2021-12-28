import math
x = float(input('Введіть число x: '))  
eps = float(input('Введіть задану точність: '))     
s = 1   
n = 1   

while True:
    a = math.pow(-1, n-1) * (math.pow(x, 2 * n-1) / math.factorial(2 * n-1)) 
    if math.fabs(a) > eps:
        s += a
        n += 1
    else:
        break
print(f'Сума: {s}')
print(f'Синус від х: {math.sin(x)}')
if s == math.sin(x):
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')
