import math
a = int(input('Введіть число:'))
b = int(input('Введіть число:'))
def get_max(a, b):
    if a > b:
        max = a
    elif a < b:
        max = b
    else:
        max = print('Суми однакові')
    return max
def get_sum(k, m, sum):
    if k > 3:
        while m < 18:
            sum += math.sin(a) ** m
            m += 2
    else:
        m = 0
        k = math.tan(k)
        sum = 15
        while m < 5:
            sum += math.tan(k)
            k = math.tan(k)
            m += 1
    return sum
sum1 = 0
sum2 = 0
sum1 = get_sum(a, 1, sum1)
sum2 = get_sum(b, 1, sum2)
max = get_max(sum1, sum2)
print('max = {0}'.format(max))
