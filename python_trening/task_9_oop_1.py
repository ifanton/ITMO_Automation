class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('input#search', 'Поиск')


class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


home = Button('button#home', 'Домой')


class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


page_name = Title('title#page_name', 'Имя страницы')


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


path = Link('link#path', 'Ссылка')

print(search.loc, search.text, home.loc, home.text, page_name.loc, page_name.text, path.loc, path.text)
