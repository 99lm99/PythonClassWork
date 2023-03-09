# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
from random import randint

m = [randint(1, 5) for i in range(5)]
n = " ".join(map(str,m))
M1 = str(max(m))
M2 = str(min(m))
print(m, n.replace(M1, M2))

# for i in n:
#     if i == "4" or i == "5":
#         n.replace("4", "1")
#         n.replace("5", "1")
#         print((n))



# res = m.replace(M, n, 5)

