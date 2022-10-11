"""Задана натуральная степень k.

Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""


import random
import os


def Polinom():
    """Запись многочлена в файл."""
    k = int(input("Enter extent: "))
    my_list = []
    for _ in range(3):  # многочлен в виде трехчлена
        my_list.append(random.randint(0, 100))
    print(my_list)
    print(f'{my_list[0]}*x**{k} + {my_list[1]}*x + {my_list[2]} = 0')

    f_path = r'reat.txt'
    with open(f_path, 'w') as f:
        f.write((f'{my_list[0]}*x**{k} + {my_list[1]}*x + {my_list[2]} = 0'))


Polinom()
