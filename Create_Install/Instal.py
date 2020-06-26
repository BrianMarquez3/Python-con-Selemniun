#Crear un Exe en python
#Automaticacion con IE
#Creacion de un .exe

from selenium import webdriver # se Improta libreria
import time

driver = webdriver.Ie(executable_path=r"D:\Automatizacion\IEDriverServer.exe")
driver.get("https://www.google.com")
time.sleep(3)
driver.close()

