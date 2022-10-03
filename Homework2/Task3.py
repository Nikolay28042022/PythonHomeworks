# Задайте список из n чисел последовательности
# (1 + 1 \ n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Enter number: "))
listA = []
sum_num = 0
for i in range(1, n + 1):
    num = (1 + 1 / i) ** i
    listA.append('{0:.3}'.format(num))
    sum_num += num
print('List: ', listA)
print('Sum = ', '{0:.3}'.format(sum_num))
