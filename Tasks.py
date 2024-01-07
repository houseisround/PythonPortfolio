""" Задача 1: Напишите программу, которая принимает на вход два числа 
и проверяет, является ли одно число квадратом другого.
Примеры:
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет 

#Решение
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

#Решение
numbers = list(map(int, input("Введите 5 чисел через пробел: ").split()))

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Максимальное число:", maximum) """


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


""" Задача 20: Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число. 

#Решение
string = input('Введите исходную строку с элементами через пробел:')
simbol = input('Введите значение для проверки его присутсвия в вышевведенной строке:')
word_list = string.split()

for i in word_list:
    for j in i:
        if j == simbol:
            print('Yes')
            exit()
print('No')"""


""" Задача 21: Напишите программу, которая определит позицию второго вхождения 
строки в списке либо сообщит, что её нет.
Пример:
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 #неверный пример
- список: [], ищем: "123", ответ: -1 

#Решение 
a = input().split()
find_str = input()
count = 0
for i in range(len(a)):
    if a[i] == find_str:
        count += 1
        if count == 2:
            print(i)
            break
else:
    print(-1)"""


""" Задача 22: Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 

# Решение 
lst = input("Введите числа через запятую:\n").split(",")  # в split по умолчанию пробел

summ = 0
print("На нечетных позициях элементы:")
for ind in range(1, len(lst), 2):
    print(lst[ind])
    summ += int(lst[ind])
print(f"Сумма элементов списка, стоящих на нечётной позиции: \n{summ}")"""


""" Задача 23: Напишите программу, которая найдёт 
произведение пар чисел списка. Парой считаем первый и 
последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]

# Решение
lst = []
for i in input("Введите числа через пробел:\n").split(): 
    lst.append(int(i))
print(lst, end=" ")

new_lst = []
for start in range(0, (len(lst)-1)//2+1):
    new_lst.append(int(lst[start])*int(lst[len(lst)-start-1]))
print(f"=> {new_lst}")"""


""" Задача 25: Напишите программу, которая будет преобразовывать
десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)"""


""" Задача 26: Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи] 

# Решение 
k = int(input())
some_list = [0] * (k * 2 + 1)
some_list[k + 1] = 1
some_list[k - 1] = 1
for ind in range(k + 2, k * 2 + 1):
    some_list[ind] = some_list[ind - 1] + some_list[ind - 2]
for ind in range(k - 2, -1, -1): #шаг -1
    some_list[ind] = some_list[ind + 2] - some_list[ind + 1]
print(some_list)"""


""" Задача 29: Задайте два числа. Напишите программу, которая найдёт НОК 
(наименьшее общее кратное) этих двух чисел. 

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for i in range(a * b, 1, -1):
    if i % a == 0 and i % b == 0:
        nok = i
print('НОК =', nok, '\n')"""


""" Задача 31: Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N 
Пример: 30 => [2,3,5]
num = int(input("Введите число: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")"""


"""Задача 32: Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности. 
Пример: [2,2,3,5] => [3,5] 
# Решение 4

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
for i in range (0, len(lst)):
   duplicate = 0
   for j in range(0, len(lst)):
       if i != j:
           if lst[i] == lst[j]:
               duplicate = 1
   if duplicate == 0:
       new_lst.append(lst[i])

print(f"Список без повторов: {new_lst}")"""


""" Задача 43: Создайте список из случаных чисел. 
Найдите максимальное количество его одинаковых элементов. 

#Решение
import random
n = int(input("Сколько элементов? "))
lst = []
for i in range(n):
    lst.append(random.randint(1,10))
print("Сформирован список: ", lst)
 
max_count = 0 
for i in range (0,len(lst)):
    if lst.count(lst[i]) > max_count:
        max_count=lst.count(lst[i])
print("Максимальное количество одинаковых элементов", max_count)"""


""" Задача 44: Создайте список из случаных чисел. Найдите второй максимум.
Пример:
а=[1,2,3] #Первый максимум == 3, второй ==2 

import random
n = int(input("Сколько элементов? "))
lst = []
for i in range(n):
    lst.append(random.randint(1,10))
print("Сформирован список: ", lst)

max_num = max (lst)
lst2 = []
for i in range(0,len(lst)):
    if lst[i] != max_num:
        lst2.append(lst[i])

max_num = max (lst2)
print(lst2, max_num)"""


""" Задача 46: Фрукты
Пользователь вводит число K - количество фруктов. 
Затем он вводит K фруктов в формате: название фрукта и его количество. 
Добавьте все фрукты в словарь, где название фрукта - это ключ, 
а количество - значение. 
Например: 
# Ввод:
>> 3 # Количество фруктов
>> Яблоко
>> 3
>> Апельсин
>> 3
>> Мандарин
>> 10
# Вывод:
>> {'Яблоко': 3, 'Апельсин': 3, 'Мандарин': 10}  

import os
os.system('cls||clear')

dictFruit = {}
amount = int(input("Введите количество фруктов: "))
for i in range(amount):
    name = input("Введите название фрукта: ")
    amountFruit = int(input("Введите количество фрукта: "))
    dictFruit[name] = amountFruit
print(dictFruit)"""


""" Задача 47: Старший и младший
Пользователь вводит число N. 
Затем он вводит личные данные (имя и возраст) своих N друзей. 
Создайте список friends и добавьте в него N словарей с ключами name и age. 
Найдите самого младшего из друзей и выведите его имя. 
Пример:
>> 3 # Количество друзей
>> Иван
>> 11
>> Саша
>> 12
>> Леша
>> 10
# Вывод:
>> Леша 

# Решение 

N = int(input("Введите количество друзей: "))
friends = []

for friend_number in range(N):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    friends.append({"name": name, "age": age})
print(friends)
min_age = friends[0]['age'] 
for some_dict in friends:
    if some_dict['age'] < min_age: 
        min_age = some_dict['age'] 
for some_dict in friends:
        if some_dict['age'] == min_age:
            print(some_dict['name'])
            break"""


""" Задача 49: Английский словарь
"Пора учить английский язык", - сказал себе Степа и решил написать 
программу для изучения английского языка. Программа получает на 
вход слово на английском языке и несколько его переводов на русском языке. 
Составьте словарь, в котором ключ - это английское слово, 
а значение - это список русских слов. В этой задаче нужно использовать
строчный метод split(). 
Пример
  Ввод:
 >> 4 # Количество слов
 >> apple - яблоко
 >> orange - оранжевый, рыжий, апельсин
 >> grape - виноград, виноградный, гроздь
 >> easy - простой, легкий, нетрудный, удобный, несложный
  Вывод:
 >> {'apple': ['яблоко'], 'orange': ['оранжевый', 'рыжий', 'апельсин'], 'grape': ['виноград', 'виноградный', 'гроздь'], 'easy': ['простой', 'легкий', 'нетрудный', 'удобный', 'несложный']}

# Решение
glossary = {}
amount = int(input("Количество слов в словаре: "))

for _ in range(amount):
    eng_rus_str = input("Введите строку из примера: \n")
    some_list = eng_rus_str.split(' - ')
    glossary[some_list[0]] = some_list[1].split(', ')

print(glossary)


eng_word = input('Введите слово для перевода: ')
if glossary.get(eng_word):
    print(', '.join(glossary.get(eng_word))) 
else:
    print('Такого слова нет')"""



"""Задача 54: Напишите игру "крестики-нолики"с двумя игроками.

список внутри списков - матрица - двумерный массив
сперва ходят крестики

def check_win_draw(some_field):
    a1 = some_field[0][0]
    a2 = some_field[0][1]
    a3 = some_field[0][2]
    b1 = some_field[1][0]
    b2 = some_field[1][1]
    b3 = some_field[1][2]
    c1 = some_field[2][0]
    c2 = some_field[2][1]
    c3 = some_field[2][2]
    if a1 == a2 == a3 != '-':
        return f'Победа {a1}'
    elif b1 == b2 == b3 != '-':
        return f'Победа {b1}'
    elif c1 == c2 == c3 != '-':
        return f'Победа {c1}'
    elif a1 == b1 == c1 != '-':
        return f'Победа {a1}'
    elif a2 == b2 == c2 != '-':
        return f'Победа {a2}'
    elif a3 == b3 == c3 != '-':
     return f'Победа {a3}'
    elif a1 == b2 == c3 != '-':
        return f'Победа {a1}'
    elif a3 == b2 == c1 != '-':
        return f'Победа {a3}'
    elif field[0].count('-') == 0 and field[1].count('-') == 0 and field[2].count('-') == 0: 
        return 'Ничья'
    else:
        return False

field = [['-' for _ in range(3)] for _ in range(3)]
for row in field: 
    for col in row: 
        print(col, end=" ") 
    print() 
print(*field, sep='\n')
letter_number = {'a': 0, 'b': 1, 'c': 2}
while True:
    x = input('Ходит Х. Введите номер клетки в формате "букву строки : номер столбца": ')
    if field[letter_number[x[0]]][int(x[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        continue
    field[letter_number[x[0]]][int(x[-1]) - 1] = 'X'
    if check_win_draw(field):
        print(check_win_draw(field))
        break  
    o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ') 
    while field[letter_number[o[0]]][int(o[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ') 
    field[letter_number[o[0]]][int(o[-1]) - 1] = '0'
    if check_win_draw(field):
        print(check_win_draw(field))
        break
    print(*field, sep='\n')
    print('Играем дальше')"""



