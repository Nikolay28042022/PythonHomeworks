"""Перевод деятичного в двоичное число.

Напишите программу, преобразующюю десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def BinariNumber():
    """Функция, переводящая десятичное число в двоичное."""
    num = int(input("Enter number: "))
    # print(bin(num))
    binary = ''
    while num > 0:
        binary += str(num % 2)
        num //= 2
    print(binary[::-1])


BinariNumber()
