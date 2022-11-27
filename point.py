# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ? 0 и Y ? 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter the coordinat point X: '))
y = int(input('Enter the coordinat point Y: '))
if x > 0 and y > 0:
    print('qarter number 1')
if x < 0 and y > 0:
    print('qarter number 2')
if x < 0 and y < 0:
    print('qarter number 3')
if x > 0 and y < 0:
    print('qarter 4')
elif x == 0 or y == 0:
    print('error')