from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")  # код для открытия конкретной странице в Chrome

# поиск элемента

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')  # задается уникальный локатор
if icon is None:
    print('Элемент 0 не найден')
else:
    print('Элемент 0 найден')

footer = driver.find_element(By.CSS_SELECTOR, 'span')
if footer is None:
    print('Элемент 1 не найден')
else:
    print('Элемент 1 найден')

card = driver.find_element(By.CSS_SELECTOR, 'div.home-body > div > div')
if card is None:
    print('Элемент 2 не найден')
else:
    print('Элемент 2 найден')