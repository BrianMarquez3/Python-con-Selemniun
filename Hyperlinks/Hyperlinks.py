# Hyperlinks
#Encuntra el link y le da Click

import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(3)
encontrar_link = driver.find_element_by_link_text('Learn PHP')
encontrar_link.click()