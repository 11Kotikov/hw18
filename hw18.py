import random
from math import floor
# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def checking_number (num_for_check):
#     while num_for_check.isdigit()==False:
#         print ("it's not possitive and integer number, pls try again: ")
#         num_for_check = input("Input possitive and integer number which is quantity of elements in your list: ")
#     else:
#         return int(num_for_check)

# def create_rand_list(num_of_el): 
#     rand_list=[]
#     if num_of_el == 0:
#         print ("You made empty list, my congratulations, weirdo")
#     else:
#         for i in range(num_of_el):
#             rand_list.append(random.randint(-8,8))
#         return rand_list

# def sum_of_the_odd_elements (iterated_list):
#     sum_el = 0
#     for i in range(1, len(iterated_list), 2):
#         sum_el +=iterated_list[i]
#     return sum_el

# user_input = checking_number(
#             input('Input possitive and integer number\
# which is quantity of elements in your list: '))
# new_list = create_rand_list(user_input)
# print (f'it\'s your new list:\n{new_list}')
# print(f'Sum of elements in odd indexes is "{sum_of_the_odd_elements(new_list)}"')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     [2, 3, 4, 5, 6] => [12, 15, 16];
#     [2, 3, 5, 6] => [12, 15]

# def checking_number (num_for_check):
#     while num_for_check.isdigit()==False:
#         print ("it's not possitive and integer number, pls try again: ")
#         num_for_check = input("Input possitive and integer number\
# which is quantity of elements in your list: ")
#     else:
#         return int(num_for_check)

# def create_rand_list(num_of_el): 
#     rand_list=[]
#     if num_of_el == 0:
#         print ("You made empty list, my congratulations, weirdo")
#     else:
#         for i in range(num_of_el):
#             rand_list.append(random.randint(2,5))
#         return rand_list

# def multiply_list_pairs (list_to_rev):
#     my_copy_list = list(reversed(list_to_rev))
#     multi_list = []
#     if len(list_to_rev)%2==0:
#         for i in range(int(len (list_to_rev)/2)):
#             multi_list.append(list_to_rev[i] * my_copy_list[i])
#     else:
#         for i in range(int((len (list_to_rev)/2)+1)):
#                 multi_list.append(list_to_rev[i] * my_copy_list[i])
#     return multi_list

# user_input = checking_number(
#             input('Input possitive and integer number\
# which is quantity of elements in your list: '))
# new_list = create_rand_list(user_input)
# print (f'it\'s your new list:\n{new_list}')
# print (f'that is your\'s multiplied list{multiply_list_pairs(new_list)}')

# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 #тут я так понимаю .0 не самое маленькое

# def checking_number (num_for_check):
#     while num_for_check.isdigit()==False:
#         print ("it's not possitive and integer number, pls try again: ")
#         num_for_check = input("Input possitive and integer number which is quantity of elements in your list: ")
#     else:
#         return int(num_for_check)

# def create_randfloat_list(num_of_el): 
#     rand_list=[]
#     if num_of_el == 0:
#         print ("You made empty list, my congratulations, weirdo")
#     else:
#         for i in range(num_of_el):
#             rand_list.append(random.uniform(1,11))
#         return rand_list

# def float_list_to_int (floattoint_list):
#     new_int_list = [floor(floattoint_list) for floattoint_list in floattoint_list]
#     return new_int_list

# def find_max (where_we_search):
#     max_num = where_we_search[0]

#     for el in range(len(where_we_search)):
#         if where_we_search[el] != 0:
#             if max_num < where_we_search[el]:
#                 max_num = where_we_search[el]
#         else:
#             None
#     return max_num

# def find_min (where_we_search):
#     min_num = where_we_search[0]

#     for el in range(len(where_we_search)):
#         if where_we_search[el] != 0:
#             if min_num > where_we_search[el]:
#                 min_num = where_we_search[el]
#         else:
#             None
#     return min_num

# user_input = checking_number(
#             input('Input possitive and integer number which\
# is quantity of elements in your list: '))

# ran_float_list = create_randfloat_list(user_input)
# ran_int_list = float_list_to_int(ran_float_list)
# new_list = []
# for i in range(len(ran_float_list)):
#     new_list.append(round(ran_float_list[i] - ran_int_list[i],4))

# print (f'The difference between min and max float number in {new_list}\
# is {round(find_max(new_list) - find_min(new_list),4)}')

#Задача 4. 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# решение номер 1:
# num = (int(input("Input int pls: ")))
# print(f" you binary for {num} is {45:b}") 

#решение номер 2(многострадальное :) и без проверок -__- ):
# def number_to_binary (num_to_bin):
#     binary_list=[]
#     while (num_to_bin>0):
#         o_l=int(float(num_to_bin%2))
#         binary_list.append(o_l)
#         num_to_bin=(num_to_bin-o_l)/2
#     return binary_list

# user_input=int(input(f'Please input positive integer number, \n{5*"please "}: '))
# print (f'Your input number was {user_input} and now it\'s in binary:')
# print (*number_to_binary (user_input),sep='')

#Задача 5 Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def checking_number (num_for_check):
#     while num_for_check.isdigit()==False:
#         print ("it's not possitive and integer number, pls try again: ")
#         num_for_check = input("Input possitive and integer number which is quantity of elements in your list: ")
#     else:
#         return int(num_for_check)

# def fibonacci (n):
#     leonardus = [i for i in range(0, 2)]
#     i = 2
#     while i < n+1:
#         leonardus.append (leonardus[i-1] + leonardus[i-2])
#         i+=1
#     return leonardus

# def negabonacci_from_fibonacci(pisanus):
#     denial = []
#     for i in range(0,len(pisanus)):
#         if i%2==0:
#             denial.append(pisanus[i]*-1)
#         else:
#             denial.append(pisanus[i])
#     return denial

# user_input = checking_number(
#             input('Input possitive and integer number to\
# create the fibonacci sequence: '))
# fib_n = fibonacci(user_input)
# nega_fib_n = negabonacci_from_fibonacci(fib_n)
# print(f'For {user_input} F(n) will be {fib_n}\
#  and negafibonacci is: {nega_fib_n}')
# nega_fib_n.pop(0)
# all_together_fibs = nega_fib_n [::-1] + fib_n
# print (f'And all together in one list!: {all_together_fibs}')