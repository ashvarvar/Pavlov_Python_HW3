###1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
### *Пример:*
### - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
### =====================================================================================================
# from random import randint

# def get_list(n, frst, last):
#     return [randint(frst, last) for i in range(n)]

# def sum_odd_position(mylist):
#     return sum(mylist[1::2])

# n = 5
# frst = 1
# last = 9

# mylist = get_list(n, frst, last)
# print(mylist)
# print(sum_odd_position(mylist))


#### 2 - Напишите программу, которая найдёт произведение пар чисел списка. 
### Парой считаем первый и последний элемент, второй и предпоследний и т.д.
### *Пример:*
### - [2, 3, 4, 5, 6] => [12, 15, 16];
### - [2, 3, 5, 6] => [12, 15]
### ===================================================================================
# from random import randint
# import math

# def get_numbers(n, frst, last):
#     return [randint(frst, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 4
# frst = 1
# last = 9

# mylist = get_numbers(n, frst, last)
# print(mylist)
# print(mult_pairs(mylist))


###  =================================================================================
### 3 - Задайте список из вещественных чисел. Напишите программу,
###  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
### *Пример:*
### - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564
### =======================================================================================
# from random import uniform

# def get_real_nums (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]

# def find_diff(mynums):
#     nums = [round(x - int(x), 2) for x in (mynums)]
#     return max(nums) - min(nums)

# n = 3
# frst = 1
# last = 9
# mynums = get_real_nums(n, frst, last)

# print (mynums)
# print(find_diff(mynums))


###========================================================================================
### 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
###*Пример:*
###- 45 -> 101101
###- 3 -> 11
###- 2 -> 10
###=========================================================================================

# n = int(input('Введите число: '))

# def conv_dec_to_bin(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]

# print(conv_dec_to_bin(n))


###=================================================================================
### 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0)
###=====================================================================================