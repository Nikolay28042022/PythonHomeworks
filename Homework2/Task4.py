# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел в одной 
# строкой.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# '0 2 4'
# res -> 3

N = int(input("Enter number: "))
pos = "0 2 4"
listA = []

for i in range(-N, N + 1):
    listA.append(i)
print(listA)
mult = listA[0] * listA[2] * listA[4]
print(mult)
