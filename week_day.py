# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter the week day: '))
if day == 6 or day == 7:
    print('weekend')
elif day < 1 or day > 7:
    print('error')
else:
 print('working day')