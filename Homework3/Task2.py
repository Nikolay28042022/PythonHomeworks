"""Напишите программу, которая найдёт произведение пар чисел списка.

Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
list_a = [2, 3, 4, 5, 6]


def MultPair(list_a):
    """Произведение пар чисел списка."""
    list_b = list_a[::-1]   # list_b = list(reversed(list_a)) -> второй способ
    list_c = []
    if len(list_a) % 2 != 0:
        for i in range(len(list_a) // 2 + 1):
            for j in range(len(list_b) // 2 + 1):
                if i == j:
                    list_c.append(list_a[i] * list_b[j])
    else:
        for i in range(len(list_a) // 2):
            for j in range(len(list_b) // 2):
                if i == j:
                    list_c.append(list_a[i] * list_b[j])
    return list_c


print(MultPair(list_a))
