# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#  1 2 3 4 5
# 3
# -> 1
from random import randint
n = int(input("add elements: "))
lst1 = [randint(0,5) for i in range(n)]
lst2 = []
print(lst1)

x = int(input("add find x: "))

for i in range(len(lst1)):

    if lst1[i] == x:
        lst2.append(lst1[i])
print(len(lst2))

