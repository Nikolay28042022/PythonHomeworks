"""Даны два файла, в каждом из которых находится запись многочлена.

Задача - сформировать файл, содержащий сумму многочленов.
"""


import os


def SumPolynom():
    """Запись суммы многочленов в третий файл."""
    a = r'reat1.txt'
    b = r'reat.txt'
    with open(a, 'r') as f:
        c = (f.readline())
    with open(b, 'r') as e:
        d = (e.readline())
    f.close()
    # print(c)
    # print(d)
    k = c.split('=')
    # print(k)
    l_1 = k[0]
    # l_2 = k[1]
    # print(l_1)
    print(f'{l_1}+ {d}')

    f_path = r'reat2.txt'
    with open(f_path, 'w') as f:
        f.write(f'{l_1} + {d}')


SumPolynom()
