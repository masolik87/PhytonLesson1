# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

x1 = float(input('Enter the coordinat x1: '))
y1 = float(input('Enter the coordinat y1: '))
x2 = float(input('Enter the coordinat x2: '))
y2 = float(input('Enter the coordinat y2: '))

distans = round (sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)
print(f'Расстояние между точками равно: {distans}')