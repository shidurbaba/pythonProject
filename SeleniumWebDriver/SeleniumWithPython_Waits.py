import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# WebElements in CSS
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)


driver.close()