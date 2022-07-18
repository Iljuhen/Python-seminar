# 1 - Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# num = input('Введите число : ')

# result = 0
# for i in range(len(num)):
#     if not num[i].isdigit():
#          continue
#     result=(int(result)+int(num[i]))
# print(f'сумма цифр в числе {num} = {result}')

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число : '))
# count = 1
# -3
# for i in range(1,N+1):
#     count = count*i
    
#     print(count, end=',')

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

# import time

# def RndNumber(len_num):
#     result = ""

#     curr_time = curr_time[3:len(curr_time)]
#     key = "489432456783"

#     for figure in curr_time:
#         result += str((int(figure) + round(time.time() * 1000)) ^ int(key[int(figure)]) % 10)
    
#     if len_num > len(result):
#         count = 1
#         while (len(result) < len_num):
#             result += str((int(result[count % 10]) * (len_num + int(curr_time) % 10)) + int(key[count % 10]) % 10)
#             count += 1
#             count *= count
#     if len_num == 1:
#         return int(result[0:len_num])
#     else:
#         rnd_num = RndNumber(1)
#         return int(result[rnd_num:len_num + rnd_num])
# print(RndNumber)