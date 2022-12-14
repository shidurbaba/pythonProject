import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.get_screenshot_as_file("scroll_to_bottom.png")
