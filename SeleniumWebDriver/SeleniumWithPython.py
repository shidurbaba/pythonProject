from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_object=Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://www.walmart.com/")
driver.back()
driver.refresh()
driver.forward()
driver.close()