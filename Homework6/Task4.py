"""Задайте список из нескольких чисел.

Напишите программу, которая найдёт сумму
элементов списка,стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


from functools import reduce


list_A = [2, 3, 5, 9, 3, 8]


def SumOddPositions(list_A):
    """Сумма элементов списка, стоящих на нечетных позициях."""
    sum_A = 0
    for i in range(len(list_A)):
        if i % 2 != 0:
            sum_A += list_A[i]
    return sum_A


# print(SumOddPositions(list_A))

sum_A = reduce(lambda a, b: a+b, list_A[1::2])
print(sum_A)
