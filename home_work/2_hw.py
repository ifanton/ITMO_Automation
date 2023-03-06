a: int = 36
b: float = 4.20
c: str = 'строка'
d: list = [1, 2, 3]
e: bool = True

print(type(a), type(b), type(c), type(d), type(e))


def task_1(a: int, b: float, c: str, d: list, e: bool) -> list:
    return a, b, c, d, e


print(task_1(a, b, c, e, d))


def task_2(f: list) -> list:
    return f


f = [1, 2, 3, 5, 8, 13, 21]  # Числа Фибоначчи

print(f[0:3])


def task_3(g: int) -> int:
    return g * g


print(task_3(3))
