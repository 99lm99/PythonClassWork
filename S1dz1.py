# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да # - 7 -> да # - 1 -> нет

number = int(input('Введите число от 1 до 7: '))


if(number == 6 or number == 7):
    print('YES')
elif(number > 7):
    print('wrong')
else:
    print('NO')