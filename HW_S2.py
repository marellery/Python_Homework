

#Задача 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# N = (input (f"Введите число: "))
# sum=0

# for i in range(len(N)):
#     if N[i] != "." and N[i] != ",":
#         sum=sum+ int(N[i])
# print(sum)




#Задача 2.  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input (f"Введите число: "))

# def multi(x):
#     if x == 1:
#         return 1
#     else:
#         return x * multi(x - 1)

# list = []
# for i in range(1, N + 1):
#     list.append(multi(i))

# print(f"Произведения чисел от 1 до {N}:  {list}")


#Задача 3.  Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input (f"Введите число: "))

# num = list(range(1, n+1))
# print(num)


# def func(n):
#     sum=0
#     for i in range(1,n):
#         num[i]=round((1+1/i)**i, 3)
#         sum=sum+num[i]
#     return sum
# print("Сумма от N: ", func(n))



#Задача 4.  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# N = int(input (f"Введите число: "))

# list = []
# for i in range(N):
#     list.append(random.randint(-N,N))
# print(list)

# f = open('HW_S1.txt', 'r')

# mult =1
# for line in f:
   
#     a=int (line)
#     if abs(a)<N:
#         mult*=list[a]
# print(mult)
# f.close()



#Задача 5.  Реализуйте алгоритм перемешивания списка.

# import random

# n = int(input (f"Введите количество элементов: "))
# list = []
# for i in range(n):
#     list.append(random.randint(1, 10))
# print(list)

# shuf=[len(list)]
# for e in range(len(list)-1):
#     shuf.append(list[e+1])
# shuf[len(list)-1]=list[0]
# print(shuf)