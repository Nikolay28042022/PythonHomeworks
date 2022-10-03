
''' Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
'''
quarter = int(input('Enter quarter: '))

if (quarter == 1):
    print('((0 <= x < &) and (0 < y < &)) or ((0 < x < &) and (0 <= y < &))')
elif (quarter == 2):
    print('(0 < x < -&) and (0 < y < &)')
elif (quarter == 3):
    print('(0 < x < -&) and (0 < y < -&)')
elif (quarter == 4):
    print('(0 < x < &) and (0 < y < -&)')
else:
    print('No coordinate')
