import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.google.com/')

time.sleep(5)                                   # Let the user actually see something!

search_box = driver.find_element(By.NAME, 'q')  # поиск по названию элемента поисковой строки - 'q'
search_box.send_keys('ChromeDriver')            # ввод текста в поисковую строку
search_box.submit()                             # подтверждение ввода

time.sleep(5)
driver.quit()
