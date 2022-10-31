import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# WebElements in CSS
driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("can")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

#for loop condition to select dyanic country
for country in countries:
    if country.text == "Canada":
        country.click()
        break

time.sleep(3)

driver.close()