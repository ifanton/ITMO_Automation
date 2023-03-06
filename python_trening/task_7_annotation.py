a: int = 5
b: str = 'строка'
C: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s #функция max - максимальное значение из диапазона от 0 до (ширина-длина значения s)


print(indent('123', 123)) #выдает число 123 через 120 пробелов от начала строки

s: str = ''

def length(s: str, width: int) -> int:
    return len(s)


print(len(s))



def longest(k: list, j: list) -> int:
    return max(len(k), len(j))


print(longest([1, 2], [1, 2, 3]))
