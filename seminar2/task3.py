# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

import random

size = int (input('Введите N '))
array = []

for i in range (size):
    k = random.randint(-100, 100)
    array.append(k)
print (array)

new_array =[]

for i in array:
    new_array.append(i)
    if i<0:
         new_array.append(0)

print (new_array)
