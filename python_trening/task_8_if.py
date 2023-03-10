# пример 1

num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

# пример 2

str1 = 'тест'
str2 = 'тест1'

if str1 in str2:
    print('ДА')
else:
    print('НЕТ')

# пример 3

num_float = 4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

# пример 4

permit_print = True

if num > 0 and permit_print:
    print('num - Положительное число')
elif not permit_print:
    print('Печать запрещена')

# пример 5

tier = int(input())

if tier >1 and tier <=4:
    print('Вы бакалавр')
elif tier > 4 and tier <= 6:
    print('Вы магистр')
elif tier > 6 and tier <= 9:
    print('Вы аспирант')
else:
    print('Введите корректный год обучения')