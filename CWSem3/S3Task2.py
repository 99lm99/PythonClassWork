# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.
from random import randint

N = int(input("add digit: "))
lst1 = [randint(0, 5) for i in range(N)]
print(lst1)

m = int(input("add digit: "))

for i in range(m):
    lst1.insert(0, lst1[-1])
    lst1.pop()

print(lst1)