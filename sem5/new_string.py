


def first_string(n:list):
    word= open('python new\Python-seminar\sem5\word.txt','w',encoding = 'utf-8' ) #encoding = 'utf-8',)
    word.write('абвгдейка - это передача')
    word.closed
    return word
'''Создание текстового файла'''

def second_string(n:list):
    word= open('D:\GeekBrains\python\python new\Python-seminar\sem5\word.txt','r',encoding = 'utf-8' )
    spisok = word.readline().split()
    word.closed
    return spisok
'''Чтение текстового файла и создание строки'''

def word_with_bug(n:list):   
    word= open('python new\Python-seminar\sem5\word.txt','r',encoding = 'utf-8' ) #encoding = 'utf-8',)
    with_bug= word.readline()
    word.closed
    print(f'изначальная строка:\n          {with_bug}')