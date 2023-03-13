# Доп задание 1
class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def starter(self):
        print('Автомобиль заведен')

    def shutdown(self):
        print('Автомобиль заглушен')

    def years(self, year_new):
        self.year = year_new

    def types(self, type_new):
        self.type = type_new

    def colors(self, color_new):
        self.color = color_new


bmw = Car('Blau', 'Coupe', '1986')

bmw.starter()
bmw.shutdown()
bmw.years('1999')
bmw.types('Sedan')
bmw.colors('Schwarz')

print(bmw.color, bmw.type, bmw.year)
