# Доп задание 1
class Car:

    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def starter(self):
        print('Автомобиль заведен')

    def shutdown(self):
        print('Автомобиль заглушен')

    def year(self):
        if not self.year:
            print('1986')

    def type(self):
        return type == 'Coupe'

    def color(self):
        return color == 'Blau'


bmw = Car()

bmw.starter()
bmw.shutdown()
bmw.year()
