import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Headless Mode


service_object = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names into BrowserSorted_VeggieList
BrowserSorted_VeggieList = []
Sorted_VeggieList = driver.find_elements(By.XPATH, "//tr/td[1]")

#sort this BrowserSortedList and should be equals to column sorted listed
for veggieElements in Sorted_VeggieList:
    BrowserSorted_VeggieList.append(veggieElements.text)
    originalSorted_VeggieList = BrowserSorted_VeggieList.copy()
    #sort sorted veggie list
    BrowserSorted_VeggieList.sort()

#assert browser sorted list from program with orginial sorted list from browser
assert BrowserSorted_VeggieList == originalSorted_VeggieList



print("execution_successful")