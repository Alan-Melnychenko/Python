n = int(input('Введіть число:'))
def sum(i):
    if i == 0 or i == 1:
        return 1
    else:
        return sum(i-1) + sum(i-2)
print('x({0}) = {1}'.format(n, sum(n)))