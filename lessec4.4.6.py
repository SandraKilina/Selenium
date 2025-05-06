import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    
    allelements = browser.find_elements(By.CLASS_NAME, "block")

    for element in allelements:
        button = element.find_element(By.CLASS_NAME, 'button')
        button.click()
        time.sleep(5)

    password = browser.find_element(By.TAG_NAME, "password")
       # password.text

    print(password.text)
    time.sleep(10)


finally:

    # Окно браузера закроется в любом случае
    browser.quit()
