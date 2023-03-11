class Mammal:
    className = 'Млекопитающее'


class Dog(Mammal):
    species = 'Canis lupus'


class Nickname(Dog):
    name = 'Pluto'


dog = Nickname()

print(dog.className)  # Млекопитающее - родительский класс
print(dog.species)  # Canis lupus - дочерний класс
print(dog.name)  # Pluto - дочерний 2-го уровня