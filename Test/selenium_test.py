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

#Produto 1
#Acesso ao Produto (Descrição)

driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click

#Adicionando produto 1 no carrinho

driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

#Carrinho e Confirmação

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click

#ConfirmaçãoP1

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Produto não se encontra no carrinho"
print("Produto se encontra no carrinho")

#Back Pagina de Vendas

driver.find_element(By.XPATH, "//#[@class='btn btn_secondary back btn medium']").click()

#Adicionando produto 2 no carrinho

driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Bike Light']").click()

driver.find_element (By.XPATH, "//*[text()='Add to cart']").click()

#Entrando no Carrinho de Compra para confirmação dos produtos 


driver.find_element (By.Х, "//a[@class=' shopping_cart _lin!']").click()
assert driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Backpack']").is_displayed(),"Produto 1 não se encontra no carrinho"
print("Produto 1 se encontra no carrinho")
assert driver.find_element (By.XPATH, "//*[@class='inventory_item_name and text()='Sauce Labs Bike Light']").is_displayed(),"Produto 2 não se encontra no carrinho"
print("Produto 2 se encontra no carrinho")
 

#Checkout

driver. find_element (By.XPATH, "//[@class='btn btn_action btn medium checkout button and text ()='Checkout]").click()

#Info Checkout


first_name = driver.find_element(By.ID, "first-name").send_keys(Rayanne)
last_name = driver.find_element(By.ID,"last-name").send_keys(Branco)
postal_code = driver.find_element(By.ID,"postal-code").send_keys(1234-567)

driver.find_element(By.ID, 'continue').click()

#Confirmação OK

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed(), "Produto 1 não se encontra no carrinho final"
print("Produto 1 se encontra no carrinho final")
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed(), "Produto 2 não se encontra no carrinho final"
print("Produto 2 se encontra no carrinho final")


#Finalização
driver.find_element (By.XPATH, "//*[@class='btn btn_action btn_medium cart _button' and text()='Finish']").click()


assert driver.find_element(By.XPATH, "//*[@class='title' and text()='Checkout: Complete']").is_displayed(),"Sua Compra não pode ser realizada"
print ("Sua Compra foi realizada com Sucesso !")




driver.quit()