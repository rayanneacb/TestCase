from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window() 

#Adicionando produto 2 no carrinho

driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Bike Light']").click()

driver.find_element (By.XPATH, "//*[text()='Add to cart']").click()

#Entrando no Carrinho de Compra para confirmação dos produtos 


driver.find_element (By.Х, "//a[@class=' shopping_cart _lin!']").click()
assert driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Backpack']").is_displayed(),"Produto 1 não se encontra no carrinho"
print("Produto 1 se encontra no carrinho")
assert driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Bike Light']").is_displayed(),"Produto 2 não se encontra no carrinho"
print("Produto 2 se encontra no carrinho")