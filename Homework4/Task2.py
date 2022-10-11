"""Простые множители числа.

Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N.
"""


def SimpleMultipliers():
    """Простые множители числа."""
    n = int(input("Enter number: "))
    i = 2    # первое простое число
    my_list = []
    while i <= n:
        if n % i == 0:
            my_list.append(i)
            n //= i
        else:
            i += 1
    print(f"Simple multipliers: {my_list}")


SimpleMultipliers()
