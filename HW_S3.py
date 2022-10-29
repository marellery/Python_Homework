# Задача 1.    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random

# n=int(input ("Введите количество элементов: "))
# list=[n]
# sum=0


# for i in range(n-1):
#     list.append(random.randint(-100,100))
# print(list)

# for i in range(1,n):
#     if i%2!=0:
#         sum+=list[i]
# print(sum)


#  Задача 2.   Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random

# n=int(input ("Введите количество элементов: "))
# list=[n]
# multilist=[]


# for i in range(n-1):
#     list.append(random.randint(-100,100))
# print(list)

# a=n/2
# print(a)
# if a%2==0:
#     for e in range(int(a)):
#         multilist.append(list[e]*list[n-1-e])
# elif a%2==1:
#     a=int(a/2+0.5)
#     for e in range(a-1):
#         multilist.append(list[e]*list[n-1-e])
#     if e==a:
#         multilist.append(list[e]*list[e])
# print(multilist)

#  Задача 3.   Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# import random

# n=int(input ("Введите количество элементов: "))
# list=[n]

# for i in range(n-1):
#     list.append(random.uniform(0,5))
# print(list)



# drobi=[]
# for i in range(n):
#     drobi.append(list[i]%1)
# print(drobi)

# for i in range(n-1):
#     min=drobi[i]
#     max=drobi[i]
#     if min>drobi[i+1]:
#         min=drobi[i+1]
#     if max<drobi[i+1]:
#         max=drobi[i+1]
# print("min=", min, "  max=", max)
# print("Разница: ",max-min)


#  Задача 4.   Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n=int(input ("Введите число для преобразования: "))
# print(bin(n)) 



#  Задача 5.   Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


# k = int(input('Введите номер элемента: '))
# fibosub = [1,-1]
# fib = [1,1]
# for i in range(2,k):
#     list = fib[i-1]+fib[i-2]
#     fib.append(list)
#     sub = fibosub[i-2] - fibosub[i-1]
#     fibosub.append(sub)
# fibosub.reverse()
# fibosub.append(0)
# print(f' Для элемента = {k} : {fibosub+fib}')

