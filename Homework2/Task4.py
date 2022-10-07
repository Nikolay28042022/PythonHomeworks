""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].

Найдите произведение элементов на указанных позициях. Позиции вводятся через
пробел в одной строкой.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
'0 2 4'
res -> 3

N = int(input("Enter number: "))

listA = []
for i in range(N):
    listA.append(int(input("Enter position: ")))
print(listA)

listB = []
for j in range(-N, N + 1):
    listB.append(j)
print(listB)

mult = 1
for i in range(N):
    for j in range(-N, N + 1):
        if listA[i] == j:
            mult *= listB[j]
print(mult) 
"""
"""
Доброго дня, отлично.
Задача 4: Немного не по условию реализовано решение. Нужно получить список из "n" элементов 
и заполнить его рандомными числами от "-n" до "n". После запросить одной строкой, через пробел 
индексы элементов и переммножить элементы, стоящие на этих индексах. Почитай про метод 
".split()": https://inlnk.ru/Qwm0Pg. Задачу зачту и рекомендую поработать с ней ещё раз.
"""

import random

n = int(input("Enter number: "))
my_list = []
for i in range(n):
    my_list.append(random.randint(-n, n))
print(my_list)

index_list = input('Enter index: ').split()
mult = 1
for j in index_list:
    mult *= my_list[int(j)]
print(mult)
