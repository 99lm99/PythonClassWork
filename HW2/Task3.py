# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input("Add digit: "))
k = 1
lst = []

while 2 ** k <= n:
    lst.append(2 ** k)
    k += 1

print(lst)

