"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

f_path = r'c:\Users\Админ\Desktop\PythonHomework\Homework5\read_2.txt'
with open(f_path, 'r', encoding='UTF-8') as f:
    text = f.read()
print(text)
text = text.split()
smb = "абв"
my_text = (' '.join([word for word in text if smb not in word]))
print(my_text)
f_path = r'c:\Users\Админ\Desktop\PythonHomework\Homework5\read_1.txt'
with open(f_path, 'w', encoding='UTF-8') as f:
    f.writelines(my_text)
