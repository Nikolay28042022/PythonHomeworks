"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

f_path = r'read_3.txt'
with open(f_path, 'r') as f:
    str_1 = f.read()
print(str_1)
count = 1
new_str = ''

for i in range(1, len(str_1)):
    if str_1[i - 1] == str_1[i]:
        count += 1
    else:
        new_str += str(count)
        new_str += str_1[i-1]
        count = 1

if str_1[i] == str_1[-1]:
    new_str += str(count)
    new_str += str_1[i]
print(new_str)
f_path = r'write_1.txt'
with open(f_path, 'w') as f:
    f.write(new_str)

str_2 = '3s3j3r1b2i2w4n4f2d3i4w'
str_3 = []
for i in range(len(str_2)):
    str_3 += str_2[i]
print(str_3)
for i in range(0, len(str_3), 2):
    j = int(str_3[i])
    mult = j * str_3[i + 1]
    print(mult, end='')
