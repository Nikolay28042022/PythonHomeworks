"""Вычислить число c заданной точностью d.

Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""


def NumberDecimalPlaces():
    """Количество десятичных знаков."""
    num = int(input('Enter number: '))
    pi = '3.1415926535897932384626433832795'

    n = pi.split('.')
    # print(n)
    pi_1 = (n[0])
    pi_2 = (n[1])
    # print(pi_2)

    my_list = []
    for i in range(num):
        my_list.append(pi_2[i])
    # print(my_list)

    s = ''.join(my_list)
    # print(s)
    print(f'{pi_1}.{s}')


NumberDecimalPlaces()
