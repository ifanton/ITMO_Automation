a, b = int(input()), int(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('Равны')


c, d = int(input()), int(input())
if c - d == 135 or d - c == 135 or c - d == - 135 or d - c == -135:
    print('YES')
else:
    print('NO')


e = int(input())
if e != 0 and e <= 2 or e == 12:
    print('Зима')
elif e != 0 and 3 <= e <= 5:
    print('Весна')
elif e != 0 and 6 <= e <= 8:
    print('Лето')
elif e != 0 and 9 <= e <= 11:
    print('Осень')


f, g, h = int(input()), int(input()), int(input())
if f > 10 and g > 10 and h > 10:
    print('YES')
else:
    print('NO')


#  дополнительное 1




#  дополнительное 2

year = int(input())
month = int(input())
print((year * 12 * 29) + (month * 29))