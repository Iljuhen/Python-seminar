# При решении не забывайте, пожалуйста, про функции: каждая задача должна быть представлена в виде 
# одной или цепочки функции
# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# "абвгдейка - это передача" = >" - это передача"


# from new_string import first_string
# from new_string import second_string
# from new_string import word_with_bug


# def word_without_bug(with_bug:list)->list:
#     bug = 'абв'
#     new_spisok = []
#     for i in with_bug:
#         if bug not in i:
#             new_spisok.append(i)
#     new_spisok = (f'{" ".join(new_spisok)}')
#     print (f'вывод после удаления бага:\n     Вариант 1: {new_spisok}')
# '''Создане строки без бага'''

# first_string(first_string)
# word_with_bug(first_string)
# word_without_bug(second_string(first_string))

# word= open('D:\GeekBrains\python\python new\Python-seminar\sem5\word.txt','r',encoding = 'utf-8' )
# var2= word.readline()
# word.closed
# '''Чтение текстового файла и создание строки для варианта 2'''

# new_list = [i for i in var2.split() if 'абв' not in i]
# print(f'     Вариант 2: {" ".join(new_list)}') 
# '''вариант 2 заработает, если убрать split из 15 строки'''
   

# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import time

player = randint(0, 1)
if player:
	print('вы начинаете')
else:
	print('начинает бот')

time.sleep(2)


def my_step(candy_left: int) -> int:
	"""По сути это и есть интеллект, который бы подошел и для бота тоже"""
	if candy_left % 29:
		return candy_left % 29
	else:
		return 28


def bot_step() -> int:
	"""А это просто рандомный бот. Смысла писать больше нет, так как выиграет все равно только первый ходящий"""
	return randint(0, 28)


candy = 2021

while candy > 0:

	if player:
		step = my_step(candy)
	else:
		step = bot_step()

	candy -= step

	if player:
		print('вы делаете ход на {}, конфет останется {}'.format(step, candy))
	else:
		print('бот делает ход на {}, конфет останется {}'.format(step, candy))

	if candy <= 0:
		if player:
			print('вы выиграли')
		else:
			print('выиграл бот')

	if player:
		player = 0
	else:
		player = 1

## 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

## 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах




# def rle_pack(raw_data: str) -> str:
#     """Упаковка данных в строку"""

#     pack = [[1, raw_data[0]]]
#     count = 1
#     index = 0
#     for i in range(1, len(raw_data)):
#         if raw_data[i] == raw_data[index]:
#             count += 1
#             pack[-1][0] = count
#             pack[-1][1] = raw_data[index]
#         else:
#             count = 1
#             index = i
#             pack.append([count, raw_data[index]])

#     res = ''
#     for i in pack:
#         res += str(i[0]) + i[1]
#     return res


# def rle_unpack(packed_data: str) -> str:
#     """Распаковка данных"""

#     res = ''
#     nums = ''
#     for i in packed_data:
#         if i.isdigit():
#             nums += i
#         else:
#             for j in range(int(nums)):
#                 res += i
#             nums = ''
#     return res



# path_1 = 'D:\GeekBrains\python\python new\Python-seminar\sem5\Rle_text.txt'
# path_2 = 'D:\GeekBrains\python\python new\Python-seminar\sem5\Rle_pack.txt'
# path_3 = 'D:\GeekBrains\python\python new\Python-seminar\sem5\Rle_unpack.txt'

# with open(path_1) as data_file:
#     data = data_file.readline()
#     print(f'исходная строка: {data}')



# result = rle_pack(data)
# with open(path_2, 'w') as data_file:
#     data_file.write(result)
# print(f'в файл {path_2} добавлены упакованные данные: {result}')


# with open(path_2) as data_file:
#     data = data_file.readline()

# result = rle_unpack(data)


# with open(path_3, 'w') as data_file:
#     data_file.write(result)
# print(f'в файл {path_3} добавлены распакованные данные: {result}')



