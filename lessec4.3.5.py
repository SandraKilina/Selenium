import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.ID, "codeInput").send_keys("Дрогон")
    time.sleep(2)
    browser.find_element(By.ID, "clickButton").click()
    time.sleep(5)
finally:

    # Окно браузера закроется в любом случае
    browser.quit()