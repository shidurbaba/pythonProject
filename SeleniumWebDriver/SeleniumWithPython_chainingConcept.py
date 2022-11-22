import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# WebElements in CSS
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)

product_names = driver.find_elements(By.CSS_SELECTOR,".products:nth-child(1) .product-name")
print(len(product_names))
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
counts = len(results)


print(counts)
assert counts > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.close()