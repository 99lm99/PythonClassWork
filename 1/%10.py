#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number = float(input('add number: '))

number = number * 10 % 10
print(int(number))
