import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Headless Mode
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-error")

service_object = Service("C:\\Users\\moses\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=service_object, options=chrome_options)
# driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

#spy and store all the webelements
product_list_element = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#chaining our way into clicking add button
#for product in product_list_element:
    #productName = product.find_element(By.XPATH, "div/h4/a").text
    #if productName == "Blackberry":
        #product.find_element(By.XPATH, "div/button").click()

#chaining our way into clicking all the products

for product in product_list_element:
    product.find_element(By.XPATH, "div/button").click()

time.sleep(3)
# driver.close()

#driver.get_screenshot_as_file("C:\\Users\\moses\\PycharmProjects\\pythonProject\\ScreenShots\\screenshot1.png")
print("execution_successful")