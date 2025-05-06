import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    button = browser.find_element(By.ID, "secret-key-button")
    button.click()
    

    time.sleep(1)
   # mykey = browser.find_element(By.ID, "text1")
    # После нажатия ищем тот же элемент заново, чтобы получить обновленные данные
    button = browser.find_element(By.ID, "secret-key-button")
    secret_key = button.get_attribute("data").strip()

   # final_key = browser.find_element(By.ID, "text2").text
    print(f" мой ключ: {secret_key}")
    time.sleep(10)


finally:

    # Окно браузера закроется в любом случае
    browser.quit()
