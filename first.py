from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time

# service_obj = Service("Users\kukaw\chromedriver_win32")
# driver = webdriver.Chrome(service=service_obj)

service_obj = Service("Users\kukaw\geckodriver-v0.33.0-win32")
driver = webdriver.Firefox(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
# print(driver.title)
# print(driver.current_url)
driver.minimize_window()
# driver.back()
# driver.refresh()
driver.forward()
time.sleep(60)
driver.close()

