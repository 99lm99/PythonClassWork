# #Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09  - A (7,-5); B (1,-1) -> 7,21


x1 = float(input("x1 - "))
y1 = float(input("y1 - "))
x2 = float(input("x2 - "))
y2 = float(input("y2 - "))
a = pow((float((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))), 1/2)
print(round((a), 3))
