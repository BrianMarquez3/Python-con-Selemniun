#Python con Selenium | Ingresar datos de correo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"D:\driverchrome\chromedriver.exe")#Ubicacion de Driver de Chrome
driver.get("https://www.gmail.com")

usuario = driver.find_element_by_id("identifierId")# Se econtro el componente
usuario.send_keys("registropsicoune@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("23mner56")
clave.send_Keys(Keys.ENTER)
#iNGRESAR A Gamil Automatiocamente