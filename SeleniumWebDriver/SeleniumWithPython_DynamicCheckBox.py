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

# WebElements in CSS
radio_buttons = driver.find_elements(By.CSS_SELECTOR, "#radio-btn-example input")
print(len(radio_buttons))

time.sleep(3)
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio1":
        radio_button.click()
        assert radio_button.is_selected()

element_display = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
hide_button = driver.find_element(By.CSS_SELECTOR, "#hide-textbox")

assert element_display.is_displayed()
hide_button.click()
time.sleep(3)

#Alert Message
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Python_Automator")
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()

time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
assert "Python_Automator" in alert.text
alert.accept()

time.sleep(3)

driver.close()
