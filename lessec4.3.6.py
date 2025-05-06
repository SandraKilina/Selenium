import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element(By.ID, "showTextBtn").click()
    

    time.sleep(1)
    get_password = browser.find_element(By.ID, "text1")
    password = get_password.get_attribute("textContent").strip()

    browser.find_element(By.ID, "userInput").send_keys(password)

    browser.find_element(By.ID, "checkBtn").click()
    time.sleep(10)
    final_key = browser.find_element(By.ID, "text2").text
    print(f"Финальный ключ: {final_key}")


finally:

    # Окно браузера закроется в любом случае
    browser.quit()