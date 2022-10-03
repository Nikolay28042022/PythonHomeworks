"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
Расстояние между двумя точками AB = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
"""

x1 = int(input("Enter coordinate x1: "))
y1 = int(input("Enter coordinate y1: "))
x2 = int(input("Enter coordinate x2: "))
y2 = int(input("Enter coordinate y2: "))

AB = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('S = ', '{0:.3}'.format(AB))
