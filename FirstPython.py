
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Создаём сервис для ChromeDriver
service = Service(ChromeDriverManager().install())

# Запускаем браузер с этим сервисом
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("http://www.facebook.com")

print("Application title is", driver.title)
print("Application URL is", driver.current_url)

driver.quit()