from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


#Validação Login e Senha

driver.find_element(By.ID, "user-name").send_keys("standard_user") #Username
driver.find_element(By.ID, "password").send_keys("secret_sauce") #Password
driver.find_element(By,"login-button").click() #Clique Login