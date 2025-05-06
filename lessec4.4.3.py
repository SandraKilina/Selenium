import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    
    parentelement = browser.find_element(By.ID, "parent_id")
    childelement = browser.find_element(By.CLASS_NAME, "child_class")
    childelement.click()
    

    time.sleep(1)

    # После нажатия ищем тот же элемент заново, чтобы получить обновленные данные
    password = browser.find_element(By.CLASS_NAME, "child_class")
    password = password.get_attribute("password").strip()

   # final_key = browser.find_element(By.ID, "text2").text
    print(f" мой ключ: {password}")
    time.sleep(10)


finally:

    # Окно браузера закроется в любом случае
    browser.quit()
