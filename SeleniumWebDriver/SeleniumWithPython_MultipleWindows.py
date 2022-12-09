import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)
#Actions_Demo

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowOpened = driver.window_handles
#Switch to Child Window
driver.switch_to.window(windowOpened[1])

new_window = driver.find_element(By.TAG_NAME, "h3").text
print(new_window)
assert "New Window" == new_window
time.sleep(2)
driver.close()

#Switch to Parent Window
driver.switch_to.window(windowOpened[0])
parent_window_text = driver.find_element(By.TAG_NAME, "h3").text
print(parent_window_text)
assert "Opening a new window" == parent_window_text
driver.close()
