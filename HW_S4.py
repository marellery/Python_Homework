

#    Задача 1.  Вычислить число c заданной точностью d

# import math

# pi = math.pi
# print('ПИ = ', pi)
# d = float(input('Введите точность расчета:'))
# print(f'Точность = {d}')
# nash_pi=4
# i=1
# while d>=nash_pi:
#     nash_pi=(nash_pi/i)+(lambda nash_pi: nash_pi=(-1):nash_pi/(i+2))
#     i=i+1
# print(f'Наш пи = {nash_pi}')  


#    Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = int(input('Введите N:'))
# M=N
# list=[]
# i=2

# while i <=N:
#     N=N%i
#     if N==0:
#         list.append(i)
#         N //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители для {M}: 1, {list}, {M}")

#    Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input('Введите количество элементов списка:'))
list=[]
unik=[]

for i in range(n):
    list.append(random.randint(1,20))
print(list)

unik.append(list[0])


for i in list:
    if list.count(i) == 1:
        unik.append(i)

print('Список неповторяющихся элементов:', unik)



#     Задача 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# from random import randint
# import itertools

# k = int(input('Введите натуральную степень:'))



# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom = get_polynomial(k, ratios)
# print(polynom)

# with open('file_4s.txt', 'w') as data:
#     data.write(polynom)
# data.close()
