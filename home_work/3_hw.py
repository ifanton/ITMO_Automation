def compare(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)


print(compare(1, -6))


def differ(c, d):
    if c - d == 135 or d - c == 135 or c - d == - 135 or d - c == -135:
        print('YES')
    else:
        print('NO')


print(differ(270, 135))


def season(e):
    if e != 0 and e <= 2 or e == 12:
        print('Зима')
    elif e != 0 and 3 <= e <= 5:
        print('Весна')
    elif e != 0 and 6 <= e <= 8:
        print('Лето')
    elif e != 0 and 9 <= e <= 11:
        print('Осень')


print(season(11))


def bigger(f, g, h):
    if f > 10 and g > 10 and h > 10:
        print('YES')
    else:
        print('NO')


print(bigger(11, 12, 9))


def positive(list_1) -> int:  # дополнительное 1
    a = 0
    for num in list_1:
        if num > 0:
            a = a + 1
    return a


print(positive([1, 2, -3, 4, 5]))


def indays(y, m) -> int:  # дополнительное 2
    return (y * 12 * 29) + (m * 29)


print(indays(2, 5))
