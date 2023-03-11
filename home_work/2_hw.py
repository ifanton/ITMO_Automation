def task_1() -> None:
    a: int = 36
    b: float = 4.20
    c: str = 'строка'
    d: list = [1, 2, 3]
    e: bool = True

    print(type(a), type(b), type(c), type(d), type(e))


task_1()


def task_2(f: list) -> list:
    return f[0:3]


f = [1, 2, 3, 5, 8, 13, 21]  # Числа Фибоначчи

print(f[0:3])


def task_3(g: int) -> int:
    return g * g


print(task_3(3))
