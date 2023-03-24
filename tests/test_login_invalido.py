from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="./chromedriver.exe")
webdriver.Chrome(service=service)

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret")
driver.find_element(By.ID, "login-button").click()
message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
assert message.text == "Epic sadface: Username and password do not match any user in this service"