import random
import pickle


n = int(input("Кількість чисел = "))
b = [random.randint(-5, 5) for i in range(n)]
with open("19(1).txt", 'wb') as file:
    pickle.dump(b, file)
with open("19(1).txt", "rb") as file:
    c = pickle.load(file)
print(c)
sum_2 = 0
for elements in c:
    if elements % 2 == 0:
        sum_2 += 1
print("Кількість парних чисел = {0}".format(sum_2))