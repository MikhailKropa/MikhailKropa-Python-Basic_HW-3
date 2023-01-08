# ЗАДАЧА 1:
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# import random

# my_list = []  # [2, 3, 5, 9, 3]

# for _ in range(10):
#     my_list.append(random.randint(0, 10))

# print(my_list)


# def sum_odd(my_list: list):
#     sum_odd_position = 0
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             sum_odd_position += my_list[i]
#     print(sum_odd_position)


# sum_odd(my_list)



# ЗАДАЧА 2:
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


# from random import randint

# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 10))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)



# ЗАДАЧА 3:
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# list1 = [1.1, 1.2, 3.1, 5.0, 10.01]
# list3 = []
# for i in range(len(list1)):
#     if round((list1[i] - int(list1[i])), 2) != 0:
#         list3.append(round((list1[i] - int(list1[i])), 2))
# print(max(list3) -  min(list3))



# ЗАДАЧА 4:
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# a = int(input())
# n = ''
# while a != 0:
#     n = str(a % 2) + n
#     a //= 2
# print(n)

# ЗАДАЧА 5:
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Введите число '))

numbers = [0,1]
for i in range(2, n + 1):
    numbers.append(numbers[i - 1] + numbers [i - 2] )

not_numbers = []
for i in range(1, n + 1):
    not_numbers.append(numbers[-i] * (-1)**(i) )
print (not_numbers + numbers)