from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.implicitly_wait(9)
driver.get("https://rahulshettyacademy.com/angularpractice")
# WebElements in CSS
name = driver.find_element(By.CSS_SELECTOR, "input[name='name']")
email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
password = driver.find_element(By.CSS_SELECTOR, "input[id='exampleInputPassword1']")
checkBox = driver.find_element(By.CSS_SELECTOR, "#exampleCheck1")
employeeRadio = driver.find_element(By.CSS_SELECTOR, "#inlineRadio2")
gender = driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")
dob = driver.find_element(By.CSS_SELECTOR, "input[name='bday']")
submit = driver.find_element(By.CSS_SELECTOR, "input[value='Submit']")
gender_dropdown = driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")

name.send_keys("Sausage Fingers")
email.send_keys("sausagefingers@junkmail.com")
password.send_keys("Password1234")

checkBox.click()
#dropdown
dropdown = Select(gender_dropdown)
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

employeeRadio.click()
dob.send_keys("09/30/1989")
submit.click()
#CSS
success_message = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible'] strong").text
print(success_message)

assert "Success" in success_message