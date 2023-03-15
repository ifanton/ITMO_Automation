from selenium import webdriver
from selenium.webdriver.common.by import By


def find_on_page():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    login = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if username is None and password is None and login is None:
        print('Элемент не найден')
    else:
        print('Элементы найдены')

find_on_page()
