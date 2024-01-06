""" Задача 1: Напишите программу, которая принимает на вход два числа 
и проверяет, является ли одно число квадратом другого.
Примеры:
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет 

number1 = int (input('Введите первое число: '))
number2 = int (input('Введите второе число: '))

if number1**2==number2 or number2**2==number1:
    print('Да, одно число квадрат другого')
else: 
    print('Нет, одно число не квадрат другого')"""


""" Задача 2: Напишите программу, которая на вход принимает 5 чисел 
и находит максимальное из них.
    
    Примеры:
    
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
 
maxx = int(input())
for _ in range(5):
    x = int(input())
    if x > maxx:
        maxx = x
print (f"{maxx} max") """


""" Задача 3: Напишите программу, которая будет на вход принимать 
число N и выводить числа от -N до N
    
    *Примеры:* 
    
    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 

number = int (input('Введите число: '))
print(*range(-number,number+1), sep=', ') """


""" Задача 4: Напишите программу, которая будет принимать на вход дробь и 
 показывать первую цифру дробной части числа.
    
    *Примеры:*
    
    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3 

a = input()
if "," in a:
    #ind = a.index(",")
    #print(a[ind+1])
    print(a[a.index(",")+1])
else:
    print('нет')"""


""" Задача 5: Напишите программу, которая принимает на 
вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30. 

n = int(input('Введите число: '))

if (n%5==0 and n%10==0 or n%15==0) and n%30!=0:
    print("Да, кратно")
else:
    print("Нет, не кратно") """


""" Задача 6: Напишите программу, которая принимает на 
вход цифру, обозначающую день недели, и проверяет, 
является ли этот день выходным.
Примеры:
- 6 -> да
- 7 -> да
- 1 -> нет 

day_of_the_week = int(
    input('Введите номер дня недели, чтобы узнать выходной это день или нет: '))

while day_of_the_week > 7 or day_of_the_week < 1:
    print('Дней недели 7. Введите число от 1 до 7: ')
    day_of_the_week = int(
        input('Введите номер дня недели, чтобы узнать выходной это день или нет: '))

if day_of_the_week == 6 or day_of_the_week == 7:
    print('Да, это выходной день')
else:
    print('Нет, это НЕ выходной день')"""


"""   Задача 8: Напишите программу, которая принимает на вход координаты точки (X и Y),
    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
    в которой находится эта точка (или на какой оси она находится).

    Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 

def GetPointArea(x, y):
    if x == 0 and y == 0:
        print("Некорректные данные, X ≠ 0 и Y ≠ 0")
    elif x == 0:
        print("Ось Y")
    elif y == 0:
        print("Ось X")
    elif x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    else:
        print("4 четверть")

x, y = int(input('Введите X: ')), int(input('Введите Y: '))

GetPointArea(x, y)"""


"""   Задача 9: Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).

def GetXYArea(chetvert):
    if chetvert == 1:
        return print("x > 0 and y > 0")
    elif chetvert == 2:
        return print("x < 0 and y > 0")
    elif chetvert == 3:
        return print("x < 0 and y < 0")
    elif chetvert == 4:
        return print("x > 0 and y < 0")
    else:
        return print("Такой четверти нет, должно быть число от 1 до 4")

import os
os.system('cls||clear')

chetvert = int(input('Введите номер четверти: '))

GetXYArea(chetvert)"""


""" Задача 11: Напишите программу, которая принимает на вход число N и 
выдаёт последовательность из N членов.
Пример:
- Для N = 5: 1, -3, 9, -27, 81 

n = int(input())
out_list = []
for i in range(n):
    out_list.append((-3) **i)
print(*out_list, sep=", ")"""


""" Задача 12: Для натурального n создать словарь индекс-значение, состоящий 
из элементов последовательности 3n + 1. 
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('введите число '))

print("{", end = " ")
for i in range(1, n):
    print(i,":", 3*i+1, end=", ")
print(n,":", 3*n+1, "}")"""


""" Задача 13: Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.

firstString = input("Первая строка: ")
secondString = input("Вторая строка: ")

max = firstString
min = secondString
if len(firstString) < len(secondString):
    max = secondString
    min = firstString

# Находим количество вхождений одной строки в другую.
print(max.count(min))"""


""" Задача 14:
Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 

def get_sum(number):
    if float(number) < 0:
        number = float(number) * (-1)

    temp_num = 0
    for i in str(number):
        if i != '.':
            temp_num += int(i)
    return temp_num

input_number = input('Введите число: ')

print(f'Сумма чисел равна {get_sum(input_number)}')"""


""" Задача 15:
Напишите программу, которая принимает на вход число 
N и выдает набор произведений чисел от 1 до N.
Пример:
Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) 

input_number = int(input('Введите число: '))
product_list = [1]

for i in range(1, input_number):
    product_list.append((i+1) * product_list[i-1])

print(product_list)"""


""" Задача 16:
Задайте список из n чисел последовательности (1 + 1/n) ** n 
и выведите на экран их сумму.
Пример:
Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06 

input_number = int(input("Введите число: "))
def get_sequence(n):
    return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(get_sequence(input_number))
print(round(sum(get_sequence(input_number)), 2))"""


"""Задача №17: Реализуйте алгоритм перемешивания списка.

import random

lst = [1, 2, 3, 4, 5]
print(f"Исходный список:\n{lst}")
random.shuffle(lst)
print(f"Список после перемешивания:\n{lst}")"""
