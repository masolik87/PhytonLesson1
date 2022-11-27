# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

qarter = int(input('Enter the qarter: '))
if qarter == 1:
    print('coordinats point x > 0, y > 0')
if qarter == 2:
    print('coordinats point x < 0, y > 0')
if qarter == 3:
    print('coordinats point x < 0, y < 0')
if qarter == 4:
    print('coordinats point x > 0, y < 0')
elif qarter < 1 or qarter > 4:
    print('error')