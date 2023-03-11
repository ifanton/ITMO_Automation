class A:

    def __init__(self):
        self.x = 10


class B(A):

    def __init__(self):
        super().__init__()  # Связь для использования аргументов из родительского класса (х)
        self.y = self.x + 5


print(B().y)  # Вызов атрибута из класса

b = B()  # Создание объекта
print(b.y)
