# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def checking_number (num_for_check):
    while num_for_check.isdigit()==False:
        print ("it's not possitive and integer number, pls try again: ")
        num_for_check = input("Input possitive and integer number which is quantity of elements in your list: ")
    else:
        return int(num_for_check)

def create_rand_list(num_of_el): 
    rand_list=[]
    if num_of_el == 0:
        print ("You made empty list, my congratulations, weirdo")
    else:
        for i in range(num_of_el):
            rand_list.append(random.randint(-8,8))
        return rand_list

def sum_of_the_odd_elements (iterated_list):
    sum_el = 0
    for i in range(1, len(iterated_list), 2):
        sum_el +=iterated_list[i]
    return sum_el

user_input = checking_number(
            input('Input possitive and integer number which is quantity of elements in your list: '))
new_list = create_rand_list(user_input)
print (f'it\'s your new list:\n{new_list}')
print(f'Sum of elements in odd positions is "{sum_of_the_odd_elements(new_list)}"')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     [2, 3, 4, 5, 6] => [12, 15, 16];
#     [2, 3, 5, 6] => [12, 15]

