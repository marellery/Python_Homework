# # предложить улучшения кода для уже решённых задач:
# 
# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import random
n = int(input('Введите количество элементов списка:'))

lst=[]
unik=[len(lst)]

for i in range(n):
    lst.append(random.randint(1,20))
print(lst)

unik[0]=lst[0]

unik=[i for i in lst if lst.count(i) == 1]
print('Список неповторяющихся элементов:', unik)


#Первоначальный вариант   


# import random
# n = int(input('Введите количество элементов списка:'))
# lst=[]
# unik=[]

# for i in range(n):
#     lst.append(random.randint(1,20))
# print(lst)

# unik.append(lst[0])


# for i in lst:
#     if lst.count(i) == 1:
#         unik.append(i)

# print('Список неповторяющихся элементов:', unik)