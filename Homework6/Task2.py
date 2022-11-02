"""Homework2. Task4."""
import random

n = int(input("Enter number: "))
# my_list = []
# for i in range(n):
#     my_list.append(random.randint(-n, n))
# print(my_list)

my_list = [random.randint(-n, n) for i in range(n)]
print(my_list)

index_list = input('Enter index: ').split()
mult = 1
for j in index_list:
    mult *= my_list[int(j)]
print(mult)
