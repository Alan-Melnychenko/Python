x1 = int(input('Введіть х1:'))
y1 = int(input('Введіть y1:'))
x2 = int(input('Введіть х2:'))
y2 = int(input('Введіть y2:'))
x3 = int(input('Введіть х3:'))
y3 = int(input('Введіть y3:'))
if ((x2-x1)**2) + ((y2-y1)**2) == ((x3-x2)**2) + ((y3-y2)**2):
    print('Трикутник рівнобедрений')
elif ((x2-x1)**2) + ((y2-y1)**2) == ((x3-x1)**2) + ((y3-y1)**2):
    print('Трикутник рівнобедрений')
elif ((x3-x2)**2) + ((y3-y2)**2) == ((x3-x1)**2) + ((y3-y1)**2):
    print('Трикутник рівнобедрений')
else:
    print('Трикутник не рівнобедрений')
