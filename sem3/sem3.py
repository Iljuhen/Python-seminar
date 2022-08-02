# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# from random import randint
# list_d = []
# for i in range(10):
#     list_d.append(randint(1,15))
# print(list_d)
# num = int(input("введите символ : "))
# for i in list_d:
#     if i==num:
#         print('такой символ есть')
#     else:
#         print('такого нет')

# 2. Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.
# import random
# import string
# random.seed(10)
# s
# list_d = []
# s = string.ascii_lowercase

# for i in range(8):
#     list_d.append(random.choice(string.ascii_lowercase))
# print(list_d)
# num = input("введите символ : ")
# for i in list_d:
#     # a=0
#     if i==num:
#         # a==i
#         print('такой символ есть',list_d.index(num))

#         # print(a)
#     else:
#         print('такого нет')

lst = ['21','1', 'er', '11','21']
find_number = 21
# count = 2#количество вхождений
def find_nuber_in_list(lst_to_seek:list,number:int,count:int = 2):
    for i in range(0,len(lst_to_seek)):   
        if lst_to_seek[i] == str(number):
            count = count-1
        if count == 0:
            return i
    return -1
pos_number = find_nuber_in_list(lst,find_number)
if pos_number != -1:
    print(pos_number)
else:
    print('в списке нет 2 вхождение')


# 3. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
