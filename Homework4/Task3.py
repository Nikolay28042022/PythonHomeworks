"""Задайте последовательность чисел.

Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.
"""


def GenerationList():
    """Генерацыия списка случайных чисел."""
    import random

    n = int(input("Enter number of list elements: "))
    my_list = []
    for i in range(n):
        my_list.append(random.randint(-n, n))
    print(my_list)

    new_list = []

    for i in range(n):
        if my_list.count(my_list[i]) < 2:
            new_list.append(my_list[i])

    print(new_list)


GenerationList()
