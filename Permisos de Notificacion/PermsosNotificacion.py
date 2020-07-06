# Permisos y Notificacion

from selenium import webdriver # se Improta libreria
from selenium.webdriver.chrome.options import Options #Enviar Acciones de teclado
import time


opciones = Options()
opciones.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notifications" : 1
})

driver = webdriver.Chrome(chrome_options=opciones, executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")
driver.get("https://www.olx.com.pe/")
time.sleep(4)