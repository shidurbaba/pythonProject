import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Headless Mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-error")

service_object = Service("C:\\Users\\moses\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#driver.get_screenshot_as_file("headlessScreenShot.png")
#driver.get_screenshot_as_file("scroll_to_bottom.png")
#driver.save_screenshot()
driver.get_screenshot_as_file("C:\\Users\\moses\\PycharmProjects\\pythonProject\\ScreenShots\\screenshot1.png")
print("execution_successful")