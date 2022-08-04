
# # 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, 
# # а вычислить, используя формулы: 
# # Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# # Пример:
# # - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1
# accuracy = ''

# def proverka (tru):
#     while True:
#         accuracy = input('Введите коэффицент точности:  ')
#         if not accuracy.isdigit():
#             continue
#         else:
#             accuracy= int(accuracy)
#             return (accuracy)
#             break
# '''Проверка на ввод именно цифры, как коэффициента''' 

# def get_pi(n: int) -> int:
    
#     num_pi = 0
#     for i in range(n):
#         num_pi +=  1/16**i*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
#     return num_pi
# '''Формула нахождения ПИ'''

# accur_num = proverka(accuracy)
# '''Добавлен коэффициент для удобства вывода'''

# result = str(get_pi(accur_num )).split('.')
# '''Разделение Пи, путем вывода его в строку и 
# делением его на две части "сплитом"- точкой'''

# print (result[0])# вывод результата до точки
# print (result[1])# вывод результата после точки

# result[1] = result[1][:accur_num ]# отсечение лишних знаков
# print (f'{result[0]}.{result[1]}')

# # 2- Задайте последовательность чисел. Напишите программу, 
# # которая выведет список неповторяющихся элементов исходной последовательности. 
# # Посмотрели, что такое множество? Вот здесь его не используйте.
# from random import randint 

# random_list=[]
# def random(first_list):
#     first_list=[]
#     for i in range(0,20):
#        first_list.append(randint(0,9))
#     return(first_list)    
# '''Создание рандомного списка'''

# main_list = random(random_list)

# def uniqum(second_list):
#     second_list = []
#     for i in main_list:
        
#         count = 0
#         for j in main_list:
#           if i==j:
#                   count +=1
#         if count==1:
#              second_list.append(i)
#     return(second_list)
# '''Создание списка из уникальных элементов рандомного списка'''
# uniqum_list = uniqum(main_list)

# def vivod():
#     print(f'{main_list} \n {uniqum_list}')
# '''Вывод на печать обоих списков'''

# vivod()


# # 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# # Пример: при N = 12 -> [2, 3]

# def proverka_number (number):
#     while True:
#         number = input('Введите число:  ')
#         if not number.isdigit():
#             continue
#         else:
#             number= int(number)
#             return (number)
#             break
# '''Проверка что введена цифра''' 

# def get_multi(number):
#     spisok_multi = []
#     divisor = 2
#     while(divisor<=number):
#         if(number % divisor) ==0:
#             spisok_multi.append(divisor)
#             number=number/divisor
#         else:
#             divisor += 1
    
#     return(spisok_multi)
# '''Вычисление простых множитилей'''

# def vivod(N):
#     print(f'простые множители числа  {N}  ->  {get_multi(N)}  ')
# '''Вывод на печать'''

# number = ''
# N = proverka_number(number)
# vivod(N)

# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.



data= "Мама сшила м0не штаны и7з бере9зовой кор45ы 893."



# word = open ('D:\GeekBrains\python\python new\Python-seminar\sem4\word.txt','r')
# print(*word)
# word.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893')
# word.close()

text =' '.join(s for s in data.split() if not any(c.isdigit() for c in s))
print(text)


# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.