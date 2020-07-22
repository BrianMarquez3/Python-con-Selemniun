# Llenar automaticamente un formulario

import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("http://127.0.0.1:5500/Llenado%20de%20Formularios/formulario.html")
time.sleep(3)

#Iniciar ciclco de autollenado de form

with open('Llenado de Formularios/datos.txt') as file:
    for i, line in enumerate(file):
        usuario = (line)
        sep = ","
        dividir = usuario.split(sep)
        try:
            gotdata = dividir[i]
            user = dividir[0]
            pas = dividir[1]
        except IndexError:
            gotdata='null'

        print(user)
        print(pas)
        driver.find_element_by_id("login").send_keys(user)
        time.sleep(2)
        driver.find_element_by_id("cont").send_keys(pas)
        time.sleep(2)
        driver.find_element_by_id("acce").click()
        time.sleep(2)

file.close()
driver.close()
