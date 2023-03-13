class Mammal:
    className = 'Млекопитающее'


class Dog(Mammal):  # В скобках ссылка на родительский класс
    species = 'Canis lupus'


class Nickname(Dog):  # В скобках ссылка на родительский класс
    name = 'Pluto'


dog = Nickname()

print(dog.className)  # Млекопитающее - родительский класс
print(dog.species)  # Canis lupus - дочерний класс
print(dog.name)  # Pluto - дочерний 2-го уровня