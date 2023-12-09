from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window() 


#Adicionando produto 1 no carrinho

driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

#Carrinho e Confirmação

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click

#ConfirmaçãoP1

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Produto não se encontra no carrinho"
print("Produto se encontra no carrinho")

#Back Pagina de Vendas

driver.find_element(By.XPATH, "//#[@class='btn btn_secondary back btn medium']").click()