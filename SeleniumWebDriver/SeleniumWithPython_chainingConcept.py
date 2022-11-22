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
actual_list = []
product_names = driver.find_elements(By.CSS_SELECTOR,".products:nth-child(1) .product-name")
print(len(product_names))
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
counts = len(results)


print(counts)
assert counts > 0

for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH, "div/button").click()

print(actual_list)
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] button").click()

#Sum my total algo
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

#total amount displayed on the screen after login
total_amount_displayed = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total_amount_displayed

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Explicit Wait Conditions:
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

promo_message=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(promo_message)

#total amount should less than discount amount
discount_amount_displayed = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(discount_amount_displayed)
assert int(float(discount_amount_displayed)) < int(total_amount_displayed)
# assert int(discount_amount_displayed) < int(total_amount_displayed)
driver.close()