#Python con Selenium | Ingresar datos de correo
#Automatizacion de secuencia de pasos

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"D:\driverchrome\chromedriver.exe")#Ubicacion de Driver de Chrome
#driver = webdriver.Firefox(executable_path=r"D:\drivermozila\geckodriver.exe")#Ubicacion de Driver de Chrome

driver.get("https://www.gmail.com")

usuario = driver.find_element_by_id("identifierId")# Se econtro el componente
usuario.send_keys("tucorreo@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("tucontraseña")
clave.send_Keys(Keys.ENTER)

#Ingresar A Gmail Automatiocamente
