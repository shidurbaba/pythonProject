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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Actions_Demo
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
actions.context_click(driver.find_element(By.CSS_SELECTOR, "a[href='#top']")).perform()
time.sleep(1)
actions.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

driver.close()