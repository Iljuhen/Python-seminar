# Домашнее задание оформляйте в виде возвращающих функций.
# Помните: то, что выдает ваша функция, может быть использовано в дальнейшем или выведено куда-то кроме консоли.

# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# spisok = [4, 7, 9, 2, 7, 8, 17, 4]

# import numbers
# from random import randint as new_rand
# spisok = [new_rand(1,15) for _ in range(new_rand(3,8))]

# def pechat(spisok_print): # печать данного списка
#     print()  # чтоб не сливалось два ответа
#     print(f'Дан список {spisok_print}')  # выводим лист, для удобства.

# def see(stripped_list):  # выводим нечетные позиции в виде нового списка для наглядности
#     result_list = []
#     for i in range(1, len(stripped_list), 2):
#         result_list.append(stripped_list[i])
#     print(
#         f'Промежуточный список из элементов с нечетными индексами \n {result_list}')

# def sum(number_list): # вычисляем сумму элементов
#     sum_numbers = 0
#     for i in range(1, len(number_list), 2):
#         sum_numbers += number_list[i]
#     return sum_numbers

# pechat(spisok)
# print()  # чтоб не сливалось два ответа
# see(spisok)
# print()  # чтоб не сливалось два ответа
# print(f'сумма элементов с нечетными индексами = {sum(spisok)}')
# print()  # чтоб не сливалось два ответа


# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint as new_rand2
# product_list = [new_rand2(1,9) for _ in range(new_rand2(3,8))]


# def prodact_of_numbers(proizv_list:list):
#     new_list = []
#     first_index = 0
#     last_index= len(proizv_list)-1
#     while last_index - first_index >=0:
#         new_list.append(proizv_list[first_index]*proizv_list[last_index])
#         first_index=first_index+1
#         last_index= last_index-1
#     return (new_list)

# def vivod (proisv_list):
#     print(proisv_list)

# vivod(f'Искомый лист :\n     {product_list}')
# print()
# vivod(f'Произведение пар :\n     {prodact_of_numbers(product_list)}')
# print()

# 3 - Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

# numbers = [1.1, 1.2, 3.1, 5.567, 10.03]

# def null_counter(num:float): 

#     '''
#     Переносит точку в числе и считает сколько знаков стоит после точки.
#     param: num - вещественное число
#     return: counter - количество символов после точки, num = int
#     '''
#     counter = 0
#     while num != int(num):
#         num*=10
#         counter = counter+1
    
#     return counter, num

# def change_list(nums: list):
#     '''    Изменяет список чисел:
#     Первый цикл: делает описанное выше, и узнает количество символов после точки
#     Второй цикл: подгоняет остальные цифры к max_counter
#     '''
#     max_counter = 0
#     counters_list = []
#     for i in range(len(nums)):
#         counter, num = null_counter(nums[i])
#         counters_list.append(counter)
#         nums[i] = num
#         if counter>max_counter:
#             max_counter = counter
#     for i in range(len(counters_list)):
#         counter = max_counter-counters_list[i]
#         if counter != max_counter:
#             nums[i]= nums[i]*10**counter
    
#     return nums, max_counter
    
# def difference_max_min(nums):
#     '''Оставляет в числах списка только вещественную часть
#     находит разницу между макс. и мин. чмслами
#     params: nums - список целых чисел
#     return: (float, float) разницы, где 1 - целая, 2- вещественная
#     '''
#     nums, max_counter = change_list(nums)
    
#     max_num, min_num = 0,nums[0]
#     for num in nums:
#         float_part = num%10**max_counter
        
#         if float_part>max_num:
#             max_num=float_part
#         if float_part<min_num:
#             min_num=float_part
#     print(f'{max_num=},{min_num=}')
#     return max_num - min_num, (max_num - min_num)/10**max_counter

# print(difference_max_min(numbers))


# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


 
while (True):
    try:
        number=int(input('Введите десятичное число: '))
        break
    except ValueError:
        print('Вы ввели не число')
        continue
'''
Вводим число и проверяем его на то что это именно число.
'''
def dec_to_bin(number):
    
    result= ""
    while(True):
        result= result+str(number%2)
        number = number//2
        if(number == 1 or number ==0):
            result += str(number)
            break
    return result[::-1]
    #print(f'{result}')    
'''
Формирует из десятичного числа -> двоичное
'''


dec_to_bin(number)
print(f'Двоичное число из {number} = {dec_to_bin(number)}')   



# 5 - Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи](https://clck.ru/sH87m)



