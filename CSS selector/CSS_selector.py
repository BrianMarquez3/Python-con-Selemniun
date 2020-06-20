#css Selector

from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)
content = driver.find_element_by_css_selector('a.w3-blue')#busqueda mediante css
content.click()