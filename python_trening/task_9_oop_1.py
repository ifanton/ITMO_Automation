# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# Выведите в консоль значение аргумента Loc, объекта search

from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc, text)
        self.loc = loc
        self.text = text


search = Input('input#search', 'Поиск')

print(search.loc)


# Добавьте к классу Input атрибут объекта text
# в этом же файле создайте:
#   Класс Button
#   Класс Title
#   Класс Link
# для каждого класса пропишите атрибуты text и loc
# создайте каждому из 4-х классов объекты, с любыми данными
# выведите в консоль text и loc  каждого класса

class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc, text)
        self.loc = loc
        self.text = text


home = Button('button#home', 'Домой')


class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc, text)
        self.loc = loc
        self.text = text


page_name = Title('title#page_name', 'Имя страницы')


class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc, text)
        self.loc = loc
        self.text = text


path = Link('link#path', 'Ссылка')

print(search.loc, search.text, home.loc, home.text, page_name.loc, page_name.text, path.loc, path.text, sep=' --- ')
print(search.check_text(), home.check_text(), page_name.check_text(), path.check_text(), sep=' --- ')
