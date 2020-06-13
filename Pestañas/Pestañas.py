#Abrir Pesatañas del Navegador Chrome


import unittest
from selenium import webdriver # se Improta libreria
from selenium.webdriver.common.keys import Keys #Enviar Acciones de teclado
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_cambiar_ventan(self):
        driver=self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")#abir un aventana en python
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])# abre una segunda pestaña 1
        driver.get("https://es.stackoverflow.com/")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])# regresa a la pantalla 0 de google
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()     