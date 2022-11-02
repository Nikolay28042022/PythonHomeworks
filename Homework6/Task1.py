"""Задача: предложить улучшения кода для уже решённых задач."""

"""С помощью использования **лямбд, filter, map, zip, enumerate,
list comprehension"""

# Генераторы списков позволяют менять исходные элементы списка. Так, следующая
#  запись приведет к тому, что все элементы списка увеличатся на единицу:

import random

a = [random.randint(-10, 10) for i in range(10)]
print(a)
a = [elements+1 for elements in a]
print(a)
[4, -2, -5, 3, 3, -4, 3, 1, -6, -6]
[5, -1, -4, 4, 4, -3, 4, 2, -5, -5]

# Homework2. Task3.
# Задайте список из n чисел последовательности
# (1 + 1 \ n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Enter number: "))
# listA = []
# sum_num = 0
# for i in range(1, n + 1):
#     num = (1 + 1 / i) ** i
#     listA.append('{0:.3}'.format(num))
#     sum_num += num
# print('List: ', listA)
# print('Sum = ', '{0:.3}'.format(sum_num))

listA = [(1 + 1 / i) ** i for i in range(1, n+1)]
print(sum(listA))
