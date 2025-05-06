import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    
    allelements = browser.find_element(By.ID, "linksContainer")
    allelements = browser.find_elements(By.CLASS_NAME, "stormtrooper")

    for element in allelements:
        result = element.find_element(By.CLASS_NAME, 'stormtrooper')
        if result == int:
            number = i+1
            i=0
        time.sleep(10)
        print(number)

    button = browser.find_element(By.ID, "checkBtn")
    
    button.send_keys(number)
    button.click()
    time.sleep(10)

    password = browser.find_element(By.TAG_NAME, "password")

    print(password.text)
    time.sleep(10)


finally:

    # Окно браузера закроется в любом случае
    browser.quit()
