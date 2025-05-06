from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # Открываем браузер и загружаем страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение X
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element
    y = calc(x)
    
    

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#treasure")
    answer_input.send_keys(y)

    # Отмечаем чекбокс "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    # Нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Ждем немного, чтобы увидеть результат
    time.sleep(10)
    
finally:
    # Закрываем браузер
    browser.quit
