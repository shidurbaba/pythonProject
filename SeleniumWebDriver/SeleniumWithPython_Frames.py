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
driver.get("https://the-internet.herokuapp.com/frames")
time.sleep(3)

#Click iFrames
driver.find_element(By.CSS_SELECTOR, "a[href='/iframe']").click()

#Swtich to Frames
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("I am sending message into frame text")

#Switch to Main Window
driver.switch_to.default_content()

header_name = driver.find_element(By.TAG_NAME, "h3").text
print(header_name)

time.sleep(3)
driver.close()
