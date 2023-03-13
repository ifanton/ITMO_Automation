# Задание 1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2 * (self.width + self.height))


one = Rectangle(10, 5)
two = Rectangle(2, 3)
three = Rectangle(100, 250)

one.square()
two.square()
three.square()

one.perimeter()
two.perimeter()
three.perimeter()

print('\n')


# Задание 2
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


example = Math(5, 10)

example.addition()
example.multiplication()
example.division()
example.subtraction()

print('\n')


# Задание 3
class Button:

    def __init__(self, text, types, loc=''):
        self.text = text
        self.type = types
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)


text_box = Button('Text Box', 'Кнопка')
check_box = Button('Check Box', 'Кнопка')
radio_button = Button('Radio Button', 'Кнопка')
web_tables = Button('Web Tables', 'Кнопка')
buttons = Button('Buttons', 'Кнопка')
links = Button('Links', 'Кнопка')
broken_links_images = Button('Broken Links - Images', 'Кнопка')
upload_and_download = Button('Upload and Download', 'Кнопка')
dynamic_properties = Button('Dynamic Properties', 'Кнопка')

print(text_box.text, check_box.text, radio_button.text, web_tables.text, buttons.text, sep=' - ')
print(links.text, broken_links_images.text, upload_and_download.text, dynamic_properties.text, sep=' - ')
print('\n')
print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())
