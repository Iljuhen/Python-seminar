#       ## 1- Определить, присутствует ли в заданном списке строк, некоторое число
#       ## Мама сшила м0не штаны и7з бере9зовой кор45ы 893.
# lst =  'Мама сшила м0не штаны и7з  бере9з0вой кор45ы 893.'
# print (lst.split())
# num = 1
# print ((any(filter(lambda i: str(num) in i, lst.split() ))), (list(filter(lambda i: str(num) in i, lst.split() ))))
# new_lst=[]
# def is_num(lst):
#     for i in lst:
#         if str(num) in i:
#             new_lst.append(i)
#             return(new_lst)
# print(is_num(lst.split()))
        
# input('Нажмите Enter, чтобы выйти') 

# # 2- Найти сумму чисел списка стоящих на нечетной позиции
# from random import randint

# n = [2, 3, 5, 9, 3]
# # sum = 0
# # for i in range(1,len(n),2):
# #     if i % 2 == 1:
# #         sum = sum + int(n[i])

# n = [randint(0, 9) for x in range(9)]
# result = [n[i] for i in range(len(n)) if i % 2 == 0]
# print(f'{n}\n{sum(result)}')

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import math
# n = [2, 3, 4, 5, 6]
# result = []
# for i in range(math.ceil(len(n)/2)):
#       result.append(int(n[i])*int(n[len(n)-1-i]))
# result = list(map(lambda i: n[i] * n[len(n) - i - 1], range((len(n) + 1) // 2)))
# print(result)

# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
from math import factorial
numm = 0
result = list([factorial(x) * (x + 1) for x in range(5)])

print(result)