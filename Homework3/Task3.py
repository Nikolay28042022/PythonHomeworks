"""Задайте список из вещественных чисел.

Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
list_a = [1.1, 1.2, 3.1, 5, 10.01]


def FractionalDifference(list_a):
    """Разница между макс и мин значением дробной части элементов."""
    list_b = []
    for i in range(len(list_a)):
        a = float(list_a[i])
        b = int(list_a[i])
        c = a - b
        list_b.append(c)
    print(list_b)
    return (max(list_b) - min(list_b))


print(FractionalDifference(list_a))
