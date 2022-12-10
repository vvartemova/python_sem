#  Напишите программу, которая принимает на вход число N и 
# выдает набор произведений (набор - это список) чисел от 1 до N.

num = int (input('Введите N '))

num_collection = []
p = 1

for i in range (1, num+1):
    p = i*p
    num_collection.append(p)
    i+=1
print (num_collection)
