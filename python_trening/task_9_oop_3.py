class Soda:

    def __init__(self, addon=None, text=''):
        self.addon = addon
        self.text = text

    def show_my_drink(self):
        if not self.addon:
            print('Обычная газировка')
        else:
            print('Газировка и', self.text)

apple_soda = Soda('apple', 'Яблоко')
cola_soda = Soda('cola', 'Кола')
pure_soda = Soda('', 'Обычная')

apple_soda.show_my_drink()
cola_soda.show_my_drink()
pure_soda.show_my_drink()
