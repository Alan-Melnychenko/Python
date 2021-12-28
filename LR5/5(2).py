a = int(input('Введіть число: '))
max = 0
while a > 1:
    b = a % 10
    a = a // 10
    if b > max:
        max = b
print('max={0}'.format(max))
