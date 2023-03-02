# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint

lst1 = [randint(0,10) for i in range(5)]
print(lst1)

m = set(lst1)
m = list(m)
print(len(m))
